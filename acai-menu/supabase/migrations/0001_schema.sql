-- ═══════════════════════════════════════════════════════════════════════════
-- AÇAÍ MENU — schema multiloja (multi-tenant)
--
-- Toda linha pertence a uma loja (store_id). Chaves estrangeiras compostas
-- (id, store_id) garantem que um produto nunca aponte para a categoria,
-- tamanho ou grupo de opções de OUTRA loja.
--
-- Segurança:
--  * RLS ativado em todas as tabelas.
--  * Visitantes (anon) só LEEM dados de lojas ativas. Nenhuma escrita pública.
--  * Escrita apenas com a chave service_role (scripts do proprietário),
--    através da função admin_sync_store().
--
-- Execute este arquivo no Supabase → SQL Editor (ou `supabase db push`).
-- É idempotente para a primeira instalação; para mudanças futuras crie 0002_*.sql.
-- ═══════════════════════════════════════════════════════════════════════════

-- gen_random_uuid() é nativo do Postgres 13+ (Supabase usa 15+).

-- ─── Tabelas ───────────────────────────────────────────────────────────────

create table if not exists public.stores (
  id               uuid primary key default gen_random_uuid(),
  slug             text not null unique check (slug ~ '^[a-z0-9]+(-[a-z0-9]+)*$' and length(slug) <= 60),
  name             text not null check (length(name) between 1 and 120),
  description      text,
  is_demo          boolean not null default false,
  is_active        boolean not null default true,
  logo_url         text,
  cover_url        text,
  primary_color    text not null default '#6B21A8' check (primary_color ~ '^#[0-9A-Fa-f]{6}$'),
  secondary_color  text not null default '#F59E0B' check (secondary_color ~ '^#[0-9A-Fa-f]{6}$'),
  whatsapp         text not null check (whatsapp ~ '^[0-9]{12,15}$'),
  instagram        text,
  address          text,
  region           text,
  maps_url         text,
  seo              jsonb not null default '{}'::jsonb,   -- {title, description, image}
  banner           jsonb not null default '{}'::jsonb,   -- {enabled, image, title, subtitle}
  opening_hours    jsonb not null default '{}'::jsonb,   -- {timezone, mode, whenClosed, ordersPaused, pausedMessage, weekly, special}
  ordering         jsonb not null default '{}'::jsonb,   -- {delivery, pickup, minOrder, deliveryTime, pickupTime, paymentMethods, pixKey}
  delivery_settings jsonb not null default '{}'::jsonb,  -- {mode, fixedFee, freeAbove, allowUnlistedNeighborhoods}
  whatsapp_message jsonb not null default '{}'::jsonb,   -- {header, footer}
  created_at       timestamptz not null default now(),
  updated_at       timestamptz not null default now()
);

create table if not exists public.categories (
  id            uuid primary key default gen_random_uuid(),
  store_id      uuid not null references public.stores(id) on delete cascade,
  key           text not null,
  name          text not null,
  description   text,
  icon          text,
  display_order int  not null default 0,
  is_active     boolean not null default true,
  unique (store_id, key),
  unique (id, store_id)
);

create table if not exists public.products (
  id               uuid primary key default gen_random_uuid(),
  store_id         uuid not null references public.stores(id) on delete cascade,
  category_id      uuid not null,
  key              text not null,
  name             text not null,
  description      text,
  image_url        text,
  price            numeric(10,2) check (price >= 0),           -- produtos sem tamanhos
  compare_at_price numeric(10,2) check (compare_at_price >= 0),
  variant_label    text,
  badges           text[] not null default '{}',
  is_featured      boolean not null default false,
  is_available     boolean not null default true,              -- false = "Indisponível"
  is_active        boolean not null default true,              -- false = oculto
  display_order    int not null default 0,
  unique (store_id, key),
  unique (id, store_id),
  foreign key (category_id, store_id) references public.categories(id, store_id) on delete cascade
);

create table if not exists public.product_variants (
  id               uuid primary key default gen_random_uuid(),
  store_id         uuid not null references public.stores(id) on delete cascade,
  product_id       uuid not null,
  key              text not null,
  name             text not null,
  description      text,
  price            numeric(10,2) not null check (price >= 0),
  compare_at_price numeric(10,2) check (compare_at_price >= 0),
  is_available     boolean not null default true,
  rules            jsonb not null default '{}'::jsonb,         -- {grupo: {min,max,free}}
  display_order    int not null default 0,
  unique (product_id, key),
  foreign key (product_id, store_id) references public.products(id, store_id) on delete cascade
);

create table if not exists public.addon_groups (
  id              uuid primary key default gen_random_uuid(),
  store_id        uuid not null references public.stores(id) on delete cascade,
  key             text not null,
  name            text not null,
  description     text,
  min_selections  int not null default 0 check (min_selections >= 0),
  max_selections  int check (max_selections is null or max_selections >= 1),
  free_selections int not null default 0 check (free_selections >= 0),
  extra_price     numeric(10,2) not null default 0 check (extra_price >= 0),
  max_per_option  int not null default 1 check (max_per_option between 1 and 20),
  display_order   int not null default 0,
  unique (store_id, key),
  unique (id, store_id)
);

create table if not exists public.addons (
  id            uuid primary key default gen_random_uuid(),
  store_id      uuid not null references public.stores(id) on delete cascade,
  group_id      uuid not null,
  key           text not null,
  name          text not null,
  description   text,
  price         numeric(10,2) not null default 0 check (price >= 0),
  always_paid   boolean not null default false,
  is_available  boolean not null default true,
  is_active     boolean not null default true,
  display_order int not null default 0,
  unique (group_id, key),
  foreign key (group_id, store_id) references public.addon_groups(id, store_id) on delete cascade
);

-- Vínculo produto ↔ grupo de opções (um grupo pode ser usado por vários produtos).
create table if not exists public.product_addon_groups (
  product_id    uuid not null,
  group_id      uuid not null,
  store_id      uuid not null references public.stores(id) on delete cascade,
  overrides     jsonb not null default '{}'::jsonb,            -- {min,max,free} só deste produto
  display_order int not null default 0,
  primary key (product_id, group_id),
  foreign key (product_id, store_id) references public.products(id, store_id) on delete cascade,
  foreign key (group_id, store_id) references public.addon_groups(id, store_id) on delete cascade
);

create table if not exists public.delivery_zones (
  id            uuid primary key default gen_random_uuid(),
  store_id      uuid not null references public.stores(id) on delete cascade,
  neighborhood  text not null,
  fee           numeric(10,2) not null check (fee >= 0),
  is_active     boolean not null default true,
  display_order int not null default 0
);

-- ─── Índices ───────────────────────────────────────────────────────────────
create index if not exists products_category_idx  on public.products (category_id);
create index if not exists variants_store_idx     on public.product_variants (store_id);
create index if not exists addons_store_idx       on public.addons (store_id);
create index if not exists pag_group_idx          on public.product_addon_groups (group_id);
create index if not exists pag_store_idx          on public.product_addon_groups (store_id);
create unique index if not exists delivery_zones_unique_idx on public.delivery_zones (store_id, lower(neighborhood));
create index if not exists stores_active_idx      on public.stores (slug) where is_active;

-- ─── updated_at automático ─────────────────────────────────────────────────
create or replace function public.touch_updated_at() returns trigger
language plpgsql as $$
begin
  new.updated_at := now();
  return new;
end $$;

drop trigger if exists stores_touch on public.stores;
create trigger stores_touch before update on public.stores
  for each row execute function public.touch_updated_at();

-- ─── Row Level Security ────────────────────────────────────────────────────
alter table public.stores               enable row level security;
alter table public.categories           enable row level security;
alter table public.products             enable row level security;
alter table public.product_variants     enable row level security;
alter table public.addon_groups         enable row level security;
alter table public.addons               enable row level security;
alter table public.product_addon_groups enable row level security;
alter table public.delivery_zones       enable row level security;

-- Leitura pública somente de lojas ativas e itens ativos.
-- (a subconsulta em "stores" também passa pelo RLS, então loja inativa = nada visível)
drop policy if exists "public read active stores" on public.stores;
create policy "public read active stores" on public.stores
  for select to anon, authenticated using (is_active);

drop policy if exists "public read categories" on public.categories;
create policy "public read categories" on public.categories
  for select to anon, authenticated
  using (is_active and store_id in (select id from public.stores));

drop policy if exists "public read products" on public.products;
create policy "public read products" on public.products
  for select to anon, authenticated
  using (is_active and store_id in (select id from public.stores));

drop policy if exists "public read variants" on public.product_variants;
create policy "public read variants" on public.product_variants
  for select to anon, authenticated
  using (store_id in (select id from public.stores));

drop policy if exists "public read addon groups" on public.addon_groups;
create policy "public read addon groups" on public.addon_groups
  for select to anon, authenticated
  using (store_id in (select id from public.stores));

drop policy if exists "public read addons" on public.addons;
create policy "public read addons" on public.addons
  for select to anon, authenticated
  using (is_active and store_id in (select id from public.stores));

drop policy if exists "public read product addon groups" on public.product_addon_groups;
create policy "public read product addon groups" on public.product_addon_groups
  for select to anon, authenticated
  using (store_id in (select id from public.stores));

drop policy if exists "public read delivery zones" on public.delivery_zones;
create policy "public read delivery zones" on public.delivery_zones
  for select to anon, authenticated
  using (is_active and store_id in (select id from public.stores));

-- Defesa extra: visitantes nunca escrevem (mesmo que alguém crie uma policy por engano).
revoke insert, update, delete, truncate on
  public.stores, public.categories, public.products, public.product_variants,
  public.addon_groups, public.addons, public.product_addon_groups, public.delivery_zones
  from anon, authenticated;
grant select on
  public.stores, public.categories, public.products, public.product_variants,
  public.addon_groups, public.addons, public.product_addon_groups, public.delivery_zones
  to anon, authenticated;

-- ═══════════════════════════════════════════════════════════════════════════
-- get_store_menu(slug) → cardápio completo de UMA loja, no mesmo formato do
-- arquivo stores/<slug>/store.json. Executa com as permissões de quem chama
-- (SECURITY INVOKER), então o RLS acima continua valendo.
-- ═══════════════════════════════════════════════════════════════════════════
create or replace function public.get_store_menu(p_slug text)
returns jsonb
language sql
stable
security invoker
set search_path = public
as $$
  select jsonb_build_object(
    'slug', s.slug,
    'name', s.name,
    'isDemo', s.is_demo,
    'active', s.is_active,
    'description', s.description,
    'seo', s.seo,
    'branding', jsonb_build_object(
      'logo', s.logo_url, 'cover', s.cover_url,
      'primaryColor', s.primary_color, 'secondaryColor', s.secondary_color),
    'banner', s.banner,
    'contact', jsonb_build_object(
      'whatsapp', s.whatsapp, 'instagram', s.instagram, 'address', s.address,
      'region', s.region, 'mapsUrl', s.maps_url),
    'hours', s.opening_hours,
    'ordering', s.ordering,
    'delivery', s.delivery_settings || jsonb_build_object('zones', coalesce((
        select jsonb_agg(jsonb_build_object('neighborhood', z.neighborhood, 'fee', z.fee, 'active', z.is_active)
                         order by z.display_order)
        from delivery_zones z where z.store_id = s.id), '[]'::jsonb)),
    'whatsappMessage', s.whatsapp_message,
    'categories', coalesce((
        select jsonb_agg(jsonb_build_object('key', c.key, 'name', c.name, 'description', c.description,
                                            'icon', c.icon, 'active', c.is_active) order by c.display_order)
        from categories c where c.store_id = s.id), '[]'::jsonb),
    'addonGroups', coalesce((
        select jsonb_agg(jsonb_build_object(
                 'key', g.key, 'name', g.name, 'description', g.description,
                 'min', g.min_selections, 'max', g.max_selections, 'free', g.free_selections,
                 'extraPrice', g.extra_price, 'maxPerOption', g.max_per_option,
                 'addons', coalesce((
                    select jsonb_agg(jsonb_build_object(
                             'key', a.key, 'name', a.name, 'description', a.description, 'price', a.price,
                             'alwaysPaid', a.always_paid, 'available', a.is_available, 'active', a.is_active)
                           order by a.display_order)
                    from addons a where a.group_id = g.id), '[]'::jsonb)
               ) order by g.display_order)
        from addon_groups g where g.store_id = s.id), '[]'::jsonb),
    'products', coalesce((
        select jsonb_agg(jsonb_strip_nulls(jsonb_build_object(
                 'key', p.key,
                 'category', c.key,
                 'name', p.name,
                 'description', p.description,
                 'image', p.image_url,
                 'price', p.price,
                 'compareAtPrice', p.compare_at_price,
                 'variantLabel', p.variant_label,
                 'badges', to_jsonb(p.badges),
                 'featured', p.is_featured,
                 'available', p.is_available,
                 'active', p.is_active,
                 'variants', (
                    select jsonb_agg(jsonb_build_object(
                             'key', v.key, 'name', v.name, 'description', v.description, 'price', v.price,
                             'compareAtPrice', v.compare_at_price, 'available', v.is_available, 'rules', v.rules)
                           order by v.display_order)
                    from product_variants v where v.product_id = p.id),
                 'addonGroups', coalesce((
                    select jsonb_agg(jsonb_build_object('group', g.key) || l.overrides order by l.display_order)
                    from product_addon_groups l join addon_groups g on g.id = l.group_id
                    where l.product_id = p.id), '[]'::jsonb)
               )) order by c.display_order, p.display_order)
        from products p join categories c on c.id = p.category_id
        where p.store_id = s.id), '[]'::jsonb)
  )
  from stores s
  where s.slug = p_slug;
$$;

grant execute on function public.get_store_menu(text) to anon, authenticated, service_role;

-- Lojas de demonstração exibidas na página inicial da plataforma.
create or replace function public.list_showcase_stores()
returns table (slug text, name text, description text, logo_url text, primary_color text, region text)
language sql stable security invoker set search_path = public
as $$
  select slug, name, description, logo_url, primary_color, region
  from stores where is_demo order by name;
$$;
grant execute on function public.list_showcase_stores() to anon, authenticated, service_role;

-- Slugs ativos (sitemap).
create or replace function public.list_store_slugs()
returns table (slug text, updated_at timestamptz)
language sql stable security invoker set search_path = public
as $$ select slug, updated_at from stores where not is_demo order by slug; $$;
grant execute on function public.list_store_slugs() to anon, authenticated, service_role;

-- ═══════════════════════════════════════════════════════════════════════════
-- admin_sync_store(payload) → cria/atualiza uma loja inteira de forma ATÔMICA
-- (tudo ou nada) a partir do JSON validado pelo script `npm run store:sync`.
-- Executável SOMENTE com a chave service_role.
-- ═══════════════════════════════════════════════════════════════════════════
create or replace function public.admin_sync_store(payload jsonb)
returns jsonb
language plpgsql
security invoker
set search_path = public
as $$
declare
  sid uuid;
  cat jsonb; grp jsonb; ad jsonb; prod jsonb; var jsonb; lnk jsonb; zn jsonb;
  ci bigint; gi bigint; ai bigint; pi bigint; vi bigint; li bigint; zi bigint;
  gid uuid; pid uuid; cid uuid; lgid uuid;
  n_products int := 0;
begin
  if payload->>'slug' is null then raise exception 'payload sem slug'; end if;

  insert into stores as st (
    slug, name, description, is_demo, is_active, logo_url, cover_url, primary_color, secondary_color,
    whatsapp, instagram, address, region, maps_url, seo, banner, opening_hours, ordering,
    delivery_settings, whatsapp_message)
  values (
    payload->>'slug', payload->>'name', payload->>'description',
    coalesce((payload->>'isDemo')::boolean, false), coalesce((payload->>'active')::boolean, true),
    payload#>>'{branding,logo}', payload#>>'{branding,cover}',
    coalesce(payload#>>'{branding,primaryColor}', '#6B21A8'), coalesce(payload#>>'{branding,secondaryColor}', '#F59E0B'),
    payload#>>'{contact,whatsapp}', payload#>>'{contact,instagram}', payload#>>'{contact,address}',
    payload#>>'{contact,region}', payload#>>'{contact,mapsUrl}',
    coalesce(payload->'seo', '{}'), coalesce(payload->'banner', '{}'), coalesce(payload->'hours', '{}'),
    coalesce(payload->'ordering', '{}'), coalesce(payload->'delivery', '{}') - 'zones',
    coalesce(payload->'whatsappMessage', '{}'))
  on conflict (slug) do update set
    name = excluded.name, description = excluded.description, is_demo = excluded.is_demo,
    is_active = excluded.is_active, logo_url = excluded.logo_url, cover_url = excluded.cover_url,
    primary_color = excluded.primary_color, secondary_color = excluded.secondary_color,
    whatsapp = excluded.whatsapp, instagram = excluded.instagram, address = excluded.address,
    region = excluded.region, maps_url = excluded.maps_url, seo = excluded.seo, banner = excluded.banner,
    opening_hours = excluded.opening_hours, ordering = excluded.ordering,
    delivery_settings = excluded.delivery_settings, whatsapp_message = excluded.whatsapp_message
  returning st.id into sid;

  -- Recria o cardápio da loja (somente desta loja).
  delete from delivery_zones where store_id = sid;
  delete from product_addon_groups where store_id = sid;
  delete from product_variants where store_id = sid;
  delete from products where store_id = sid;
  delete from addons where store_id = sid;
  delete from addon_groups where store_id = sid;
  delete from categories where store_id = sid;

  for cat, ci in select * from jsonb_array_elements(coalesce(payload->'categories', '[]')) with ordinality loop
    insert into categories (store_id, key, name, description, icon, display_order, is_active)
    values (sid, cat->>'key', cat->>'name', cat->>'description', cat->>'icon', ci,
            coalesce((cat->>'active')::boolean, true));
  end loop;

  for grp, gi in select * from jsonb_array_elements(coalesce(payload->'addonGroups', '[]')) with ordinality loop
    insert into addon_groups (store_id, key, name, description, min_selections, max_selections,
                              free_selections, extra_price, max_per_option, display_order)
    values (sid, grp->>'key', grp->>'name', grp->>'description',
            coalesce((grp->>'min')::int, 0), (grp->>'max')::int, coalesce((grp->>'free')::int, 0),
            coalesce((grp->>'extraPrice')::numeric, 0), coalesce((grp->>'maxPerOption')::int, 1), gi)
    returning id into gid;
    for ad, ai in select * from jsonb_array_elements(coalesce(grp->'addons', '[]')) with ordinality loop
      insert into addons (store_id, group_id, key, name, description, price, always_paid, is_available, is_active, display_order)
      values (sid, gid, ad->>'key', ad->>'name', ad->>'description', coalesce((ad->>'price')::numeric, 0),
              coalesce((ad->>'alwaysPaid')::boolean, false), coalesce((ad->>'available')::boolean, true),
              coalesce((ad->>'active')::boolean, true), ai);
    end loop;
  end loop;

  for prod, pi in select * from jsonb_array_elements(coalesce(payload->'products', '[]')) with ordinality loop
    select id into cid from categories where store_id = sid and key = prod->>'category';
    if cid is null then
      raise exception 'produto "%": categoria "%" não existe', prod->>'key', prod->>'category';
    end if;
    insert into products (store_id, category_id, key, name, description, image_url, price, compare_at_price,
                          variant_label, badges, is_featured, is_available, is_active, display_order)
    values (sid, cid, prod->>'key', prod->>'name', prod->>'description', prod->>'image',
            (prod->>'price')::numeric, (prod->>'compareAtPrice')::numeric, prod->>'variantLabel',
            coalesce(array(select jsonb_array_elements_text(coalesce(prod->'badges', '[]')))::text[], '{}'),
            coalesce((prod->>'featured')::boolean, false), coalesce((prod->>'available')::boolean, true),
            coalesce((prod->>'active')::boolean, true), pi)
    returning id into pid;
    n_products := n_products + 1;

    for var, vi in select * from jsonb_array_elements(coalesce(prod->'variants', '[]')) with ordinality loop
      insert into product_variants (store_id, product_id, key, name, description, price, compare_at_price,
                                    is_available, rules, display_order)
      values (sid, pid, var->>'key', var->>'name', var->>'description', (var->>'price')::numeric,
              (var->>'compareAtPrice')::numeric, coalesce((var->>'available')::boolean, true),
              coalesce(var->'rules', '{}'), vi);
    end loop;

    for lnk, li in select * from jsonb_array_elements(coalesce(prod->'addonGroups', '[]')) with ordinality loop
      if jsonb_typeof(lnk) = 'string' then
        lnk := jsonb_build_object('group', lnk #>> '{}');
      end if;
      select id into lgid from addon_groups where store_id = sid and key = lnk->>'group';
      if lgid is null then
        raise exception 'produto "%": grupo "%" não existe', prod->>'key', lnk->>'group';
      end if;
      insert into product_addon_groups (product_id, group_id, store_id, overrides, display_order)
      values (pid, lgid, sid, lnk - 'group', li);
    end loop;
  end loop;

  for zn, zi in select * from jsonb_array_elements(coalesce(payload#>'{delivery,zones}', '[]')) with ordinality loop
    insert into delivery_zones (store_id, neighborhood, fee, is_active, display_order)
    values (sid, zn->>'neighborhood', (zn->>'fee')::numeric, coalesce((zn->>'active')::boolean, true), zi);
  end loop;

  return jsonb_build_object('store_id', sid, 'slug', payload->>'slug', 'products', n_products);
end $$;

revoke all on function public.admin_sync_store(jsonb) from public;
revoke all on function public.admin_sync_store(jsonb) from anon, authenticated;
grant execute on function public.admin_sync_store(jsonb) to service_role;

-- Remover uma loja (e todo o seu cardápio). Somente service_role.
create or replace function public.admin_delete_store(p_slug text)
returns boolean language sql security invoker set search_path = public
as $$ with d as (delete from stores where slug = p_slug returning 1) select exists(select 1 from d); $$;
revoke all on function public.admin_delete_store(text) from public;
revoke all on function public.admin_delete_store(text) from anon, authenticated;
grant execute on function public.admin_delete_store(text) to service_role;
