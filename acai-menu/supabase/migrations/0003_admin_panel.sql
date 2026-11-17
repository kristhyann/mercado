-- ═══════════════════════════════════════════════════════════════════════════
-- AÇAÍ MENU — Painel administrativo do proprietário da plataforma
--
-- * platform_admins: lista de usuários (Supabase Auth) com acesso ao painel.
--   Comerciantes NÃO têm login. Cadastre apenas você (npm run admin:create).
-- * Todas as funções admin_* verificam no banco se quem chama é administrador
--   (ou a chave service_role dos scripts). O painel usa a sessão do
--   administrador: a service_role NÃO precisa ficar na Vercel.
-- * As tabelas continuam sem nenhuma permissão de escrita para anon/authenticated:
--   escrita só acontece dentro destas funções.
--
-- Execute depois de 0001 e 0002. Não apaga nem altera dados existentes.
-- ═══════════════════════════════════════════════════════════════════════════

create table if not exists public.platform_admins (
  user_id    uuid primary key references auth.users(id) on delete cascade,
  email      text,
  created_at timestamptz not null default now()
);
alter table public.platform_admins enable row level security;
-- Sem policies: ninguém lê ou altera esta tabela pela API. Só funções SECURITY DEFINER.
revoke all on public.platform_admins from anon, authenticated;

-- Quem chama é administrador da plataforma?
create or replace function public.is_platform_admin()
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (select 1 from public.platform_admins where user_id = auth.uid());
$$;
revoke all on function public.is_platform_admin() from public, anon;
grant execute on function public.is_platform_admin() to authenticated, service_role;

-- Papel da requisição (anon / authenticated / service_role) segundo o JWT do Supabase.
create or replace function public.request_role()
returns text
language sql
stable
as $$
  select coalesce(
    nullif(current_setting('request.jwt.claim.role', true), ''),
    nullif(current_setting('request.jwt.claims', true), '')::jsonb ->> 'role'
  );
$$;

-- Bloqueia quem não for administrador. Permitido: administrador logado, chave
-- service_role (scripts) e o SQL Editor do Supabase (usuário postgres, sem JWT).
create or replace function public.assert_platform_admin()
returns void
language plpgsql
stable
security definer
set search_path = public
as $$
declare
  r text := public.request_role();
begin
  if r = 'service_role' then return; end if;
  if r is null and session_user = 'postgres' then return; end if;
  if public.is_platform_admin() then return; end if;
  raise exception 'acesso negado: somente o administrador da plataforma' using errcode = '42501';
end $$;
revoke all on function public.assert_platform_admin() from public, anon;
grant execute on function public.assert_platform_admin() to authenticated, service_role;

-- ─── admin_sync_store: nova versão (verifica administrador + edição simultânea) ─
-- A versão de 0001 recebia só (payload). Esta aceita também a versão esperada da
-- loja: se outra aba/aparelho salvou antes, a gravação é recusada em vez de
-- sobrescrever as alterações.
do $$
begin
  -- Renomeia a versão antiga (só na primeira execução desta migração).
  if to_regprocedure('public.admin_sync_store(jsonb)') is not null then
    if to_regprocedure('public.admin_sync_store_impl(jsonb)') is not null then
      drop function public.admin_sync_store_impl(jsonb);
    end if;
    alter function public.admin_sync_store(jsonb) rename to admin_sync_store_impl;
  end if;
end $$;
revoke all on function public.admin_sync_store_impl(jsonb) from public, anon, authenticated, service_role;
alter function public.admin_sync_store_impl(jsonb) security definer;

create or replace function public.admin_sync_store(payload jsonb, expected_updated_at text default null)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  current_version timestamptz;
  result jsonb;
begin
  perform public.assert_platform_admin();
  if expected_updated_at is not null then
    select updated_at into current_version from stores where slug = payload->>'slug';
    if current_version is not null and current_version <> expected_updated_at::timestamptz then
      raise exception 'conflito: esta loja foi alterada em outro lugar. Recarregue a página para ver a versão atual.'
        using errcode = '40001';
    end if;
  end if;
  result := public.admin_sync_store_impl(payload);
  return result || jsonb_build_object(
    'updated_at', (select updated_at::text from stores where slug = payload->>'slug'));
end $$;
revoke all on function public.admin_sync_store(jsonb, text) from public, anon;
grant execute on function public.admin_sync_store(jsonb, text) to authenticated, service_role;

-- ─── Leitura completa de uma loja para o painel (inclui itens inativos) ──────
create or replace function public.admin_get_store(p_slug text)
returns jsonb
language plpgsql
stable
security definer
set search_path = public
as $$
declare
  s record;
begin
  perform public.assert_platform_admin();
  select slug, updated_at::text as updated_at, created_at::text as created_at into s from stores where slug = p_slug;
  if not found then return null; end if;
  return jsonb_build_object(
    'config', public.get_store_menu(p_slug),
    'updated_at', s.updated_at,
    'created_at', s.created_at);
end $$;
revoke all on function public.admin_get_store(text) from public, anon;
grant execute on function public.admin_get_store(text) to authenticated, service_role;

-- ─── Lista de lojas + contagens (dashboard) ─────────────────────────────────
create or replace function public.admin_list_stores()
returns table (
  slug text, name text, is_active boolean, is_demo boolean, logo_url text, primary_color text,
  whatsapp text, created_at timestamptz, updated_at text, product_count int, active_product_count int,
  category_count int)
language plpgsql
stable
security definer
set search_path = public
as $$
begin
  perform public.assert_platform_admin();
  return query
    select s.slug, s.name, s.is_active, s.is_demo, s.logo_url, s.primary_color, s.whatsapp, s.created_at,
           s.updated_at::text,
           (select count(*)::int from products p where p.store_id = s.id),
           (select count(*)::int from products p where p.store_id = s.id and p.is_active),
           (select count(*)::int from categories c where c.store_id = s.id)
    from stores s
    order by s.created_at desc;
end $$;
revoke all on function public.admin_list_stores() from public, anon;
grant execute on function public.admin_list_stores() to authenticated, service_role;

-- ─── Ativar / desativar loja ────────────────────────────────────────────────
create or replace function public.admin_set_store_active(p_slug text, p_active boolean)
returns text
language plpgsql
security definer
set search_path = public
as $$
declare
  v text;
begin
  perform public.assert_platform_admin();
  update stores set is_active = p_active where slug = p_slug returning updated_at::text into v;
  if v is null then raise exception 'loja "%" não encontrada', p_slug; end if;
  return v;
end $$;
revoke all on function public.admin_set_store_active(text, boolean) from public, anon;
grant execute on function public.admin_set_store_active(text, boolean) to authenticated, service_role;

-- ─── Alterar o endereço (slug) de uma loja ──────────────────────────────────
create or replace function public.admin_rename_store(p_old text, p_new text)
returns text
language plpgsql
security definer
set search_path = public
as $$
declare
  v text;
begin
  perform public.assert_platform_admin();
  if p_new !~ '^[a-z0-9]+(-[a-z0-9]+)*$' or length(p_new) > 60 then
    raise exception 'endereço inválido: use letras minúsculas, números e hífens';
  end if;
  if exists (select 1 from stores where slug = p_new) then
    raise exception 'o endereço "%" já está em uso', p_new;
  end if;
  update stores set slug = p_new where slug = p_old returning updated_at::text into v;
  if v is null then raise exception 'loja "%" não encontrada', p_old; end if;
  return v;
end $$;
revoke all on function public.admin_rename_store(text, text) from public, anon;
grant execute on function public.admin_rename_store(text, text) to authenticated, service_role;

-- ─── Excluir loja: agora também liberado para o administrador logado ─────────
create or replace function public.admin_delete_store(p_slug text)
returns boolean
language plpgsql
security definer
set search_path = public
as $$
declare
  n int;
begin
  perform public.assert_platform_admin();
  delete from stores where slug = p_slug;
  get diagnostics n = row_count;
  return n > 0;
end $$;
revoke all on function public.admin_delete_store(text) from public, anon;
grant execute on function public.admin_delete_store(text) to authenticated, service_role;

-- ─── Storage: somente o administrador envia, substitui e exclui imagens ──────
-- (a leitura das imagens continua pública porque o bucket é público)
drop policy if exists "acai admin insert assets" on storage.objects;
create policy "acai admin insert assets" on storage.objects
  for insert to authenticated
  with check (bucket_id = 'store-assets' and public.is_platform_admin());

drop policy if exists "acai admin update assets" on storage.objects;
create policy "acai admin update assets" on storage.objects
  for update to authenticated
  using (bucket_id = 'store-assets' and public.is_platform_admin())
  with check (bucket_id = 'store-assets' and public.is_platform_admin());

drop policy if exists "acai admin delete assets" on storage.objects;
create policy "acai admin delete assets" on storage.objects
  for delete to authenticated
  using (bucket_id = 'store-assets' and public.is_platform_admin());

drop policy if exists "acai admin list assets" on storage.objects;
create policy "acai admin list assets" on storage.objects
  for select to authenticated
  using (bucket_id = 'store-assets' and public.is_platform_admin());

-- Painel envia apenas imagens otimizadas (WebP). SVG continua aceito só pelos scripts.
update storage.buckets
   set allowed_mime_types = array['image/jpeg', 'image/png', 'image/webp', 'image/avif', 'image/svg+xml', 'image/gif']
 where id = 'store-assets';

-- ═══════════════════════════════════════════════════════════════════════════
-- Para tornar um usuário administrador manualmente (alternativa ao script):
--   insert into public.platform_admins (user_id, email)
--   select id, email from auth.users where email = 'voce@exemplo.com';
-- ═══════════════════════════════════════════════════════════════════════════
