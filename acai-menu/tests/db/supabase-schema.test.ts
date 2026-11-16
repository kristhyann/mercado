/**
 * Testa as migrações SQL em um Postgres real (PGlite, em memória),
 * simulando os papéis do Supabase (anon, authenticated, service_role).
 */
import { PGlite } from "@electric-sql/pglite";
import fs from "node:fs";
import path from "node:path";
import { beforeAll, describe, expect, it } from "vitest";
import { parseStore } from "@/lib/menu";
import { toSyncPayload } from "@/lib/sync-payload";

const root = path.resolve(__dirname, "../..");
const readStore = (slug: string) => JSON.parse(fs.readFileSync(path.join(root, "stores", slug, "store.json"), "utf8"));

let db: PGlite;

async function as<T>(role: "anon" | "service_role", fn: () => Promise<T>): Promise<T> {
  await db.exec(`set role ${role}`);
  try {
    return await fn();
  } finally {
    await db.exec("reset role");
  }
}

async function sync(slug: string, mutate?: (cfg: any) => void) {
  const raw = readStore(slug);
  mutate?.(raw);
  const { config, issues } = parseStore(raw, { strict: true });
  expect(issues.filter((i) => !i.startsWith("aviso"))).toEqual([]);
  const payload = toSyncPayload(config!);
  return as("service_role", () => db.query<{ r: any }>("select public.admin_sync_store($1::jsonb) as r", [JSON.stringify(payload)]));
}

async function menuAsAnon(slug: string) {
  const res = await as("anon", () => db.query<{ m: any }>("select public.get_store_menu($1) as m", [slug]));
  return res.rows[0]?.m ?? null;
}

beforeAll(async () => {
  db = new PGlite();
  // Ambiente mínimo equivalente ao Supabase.
  await db.exec(`
    create role anon nologin;
    create role authenticated nologin;
    create role service_role nologin bypassrls;
    grant usage on schema public to anon, authenticated, service_role;
    alter default privileges in schema public grant all on tables to anon, authenticated, service_role;
    alter default privileges in schema public grant all on functions to anon, authenticated, service_role;
    create schema storage;
    create table storage.buckets (id text primary key, name text, public boolean, file_size_limit bigint, allowed_mime_types text[]);
  `);
  for (const f of fs.readdirSync(path.join(root, "supabase/migrations")).sort()) {
    await db.exec(fs.readFileSync(path.join(root, "supabase/migrations", f), "utf8"));
  }
  await db.exec("grant all on all tables in schema public to service_role;");
});

describe("schema Supabase", () => {
  it("cadastra lojas diferentes de forma atômica", async () => {
    for (const slug of ["acai-da-maria", "acai-tropical", "acai-premium"]) {
      const res = await sync(slug);
      expect(res.rows[0].r.slug).toBe(slug);
    }
    const count = await db.query<{ n: number }>("select count(*)::int as n from stores");
    expect(count.rows[0].n).toBe(3);
  });

  it("get_store_menu devolve o mesmo cardápio do arquivo JSON", async () => {
    for (const slug of ["acai-da-maria", "acai-tropical", "acai-premium"]) {
      const fromDb = parseStore(await menuAsAnon(slug));
      const fromFile = parseStore(readStore(slug));
      expect(fromDb.issues).toEqual([]);
      expect(fromDb.menu).toEqual(fromFile.menu);
    }
  });

  it("cada loja só enxerga os próprios produtos", async () => {
    const maria = parseStore(await menuAsAnon("acai-da-maria")).menu!;
    const tropical = parseStore(await menuAsAnon("acai-tropical")).menu!;
    const keys = (m: typeof maria) => m.categories.flatMap((c) => c.products.map((p) => p.name));
    expect(keys(maria)).toContain("Monte seu açaí");
    expect(keys(maria)).not.toContain("Açaí Havaiano");
    expect(keys(tropical)).toContain("Açaí Havaiano");
    expect(keys(tropical)).not.toContain("Combo Família — 1 litro + 2 copos 300 ml");
  });

  it("sincronizar de novo atualiza preços sem duplicar", async () => {
    await sync("acai-tropical", (cfg) => {
      cfg.products[0].variants[0].price = 14.5;
    });
    const menu = parseStore(await menuAsAnon("acai-tropical")).menu!;
    expect(menu.categories[0].products[0].variants[0].price).toBe(1450);
    const n = await db.query<{ n: number }>("select count(*)::int as n from products p join stores s on s.id = p.store_id where s.slug = 'acai-tropical'");
    expect(n.rows[0].n).toBe(readStore("acai-tropical").products.length);
  });

  it("visitante não vê loja inativa nem itens inativos", async () => {
    await sync("acai-premium", (cfg) => {
      cfg.products.find((p: any) => p.key === "brownie").active = false;
    });
    const premium = parseStore(await menuAsAnon("acai-premium")).menu!;
    expect(premium.categories.flatMap((c) => c.products.map((p) => p.key))).not.toContain("brownie");

    await sync("acai-premium", (cfg) => {
      cfg.active = false;
    });
    expect(await menuAsAnon("acai-premium")).toBeNull();
    const slugs = await as("anon", () => db.query<{ slug: string }>("select slug from public.list_store_slugs()"));
    expect(slugs.rows.map((r) => r.slug)).not.toContain("acai-premium");
    await sync("acai-premium");
  });

  it("visitante (anon) não consegue escrever nem chamar funções administrativas", async () => {
    await expect(as("anon", () => db.query("insert into stores (slug, name, whatsapp) values ('hacker', 'x', '5511999999999')"))).rejects.toThrow();
    await expect(as("anon", () => db.query("update products set name = 'x'"))).rejects.toThrow();
    await expect(as("anon", () => db.query("delete from stores"))).rejects.toThrow();
    await expect(as("anon", () => db.query("select public.admin_sync_store('{}'::jsonb)"))).rejects.toThrow(/permission denied/);
    await expect(as("anon", () => db.query("select public.admin_delete_store('acai-da-maria')"))).rejects.toThrow(/permission denied/);
  });

  it("impede vincular produto à categoria de outra loja", async () => {
    await expect(
      db.query(`
        insert into products (store_id, category_id, key, name, price)
        select (select id from stores where slug = 'acai-tropical'),
               (select c.id from categories c join stores s on s.id = c.store_id where s.slug = 'acai-da-maria' limit 1),
               'invasor', 'Invasor', 10`),
    ).rejects.toThrow(/foreign key/);
  });

  it("sync com erro não altera nada (tudo ou nada)", async () => {
    const before = await menuAsAnon("acai-tropical");
    const raw = readStore("acai-tropical");
    const payload: any = toSyncPayload(parseStore(raw).config!);
    payload.products[1].category = "categoria-inexistente";
    await expect(as("service_role", () => db.query("select public.admin_sync_store($1::jsonb)", [JSON.stringify(payload)]))).rejects.toThrow(/categoria/);
    expect(await menuAsAnon("acai-tropical")).toEqual(before);
  });

  it("cria o bucket público de imagens", async () => {
    const b = await db.query<{ public: boolean }>("select public from storage.buckets where id = 'store-assets'");
    expect(b.rows[0].public).toBe(true);
  });
});
