-- ═══════════════════════════════════════════════════════════════════════════
-- Supabase Storage: bucket público para logos, capas, banners e fotos.
-- Leitura pública (as imagens aparecem no cardápio); upload SOMENTE com a
-- chave service_role, usada pelo script `npm run store:sync`.
-- Organização: store-assets/<slug-da-loja>/<arquivo>
-- ═══════════════════════════════════════════════════════════════════════════
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values (
  'store-assets', 'store-assets', true, 5242880,
  array['image/jpeg', 'image/png', 'image/webp', 'image/avif', 'image/svg+xml', 'image/gif']
)
on conflict (id) do update set
  public = excluded.public,
  file_size_limit = excluded.file_size_limit,
  allowed_mime_types = excluded.allowed_mime_types;

-- Não criamos policies de INSERT/UPDATE/DELETE para anon/authenticated:
-- com RLS ativo em storage.objects, apenas a service_role consegue enviar arquivos.
