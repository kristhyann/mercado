/**
 * Formato de configuração de uma loja (arquivo stores/<slug>/store.json).
 *
 * Este é o "contrato" único do sistema:
 *  - os arquivos JSON da pasta /stores seguem este formato;
 *  - o script `npm run store:sync` envia este formato para o Supabase;
 *  - a função SQL `get_store_menu(slug)` devolve exatamente este formato;
 *  - o site valida tudo com este schema antes de exibir.
 *
 * Preços são informados em reais (ex.: 12.5 = R$ 12,50).
 */
import { z } from "zod";

const KEY = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const key = z.string().regex(KEY, "use apenas letras minúsculas, números e hífens (ex.: acai-500ml)");
const money = z.number().min(0).max(100000);
const hexColor = z.string().regex(/^#([0-9a-fA-F]{6})$/, "use cor hexadecimal com 6 dígitos (ex.: #6B21A8)");
const time = z.string().regex(/^([01]\d|2[0-3]):[0-5]\d$/, "use HH:MM (ex.: 14:00)");
const optionalText = z.string().trim().max(2000).nullish().transform((v) => (v ? v : null));
const imageRef = z.string().trim().max(1000).nullish().transform((v) => (v ? v : null));

export const RESERVED_SLUGS = new Set([
  "api", "admin", "_next", "static", "public", "images", "demo", "sitemap.xml", "robots.txt",
  "favicon.ico", "icon", "apple-icon", "opengraph-image", "manifest", "login", "checkout",
]);

export const intervalSchema = z.object({ open: time, close: time });
export type Interval = z.infer<typeof intervalSchema>;

export const WEEKDAYS = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"] as const;
export type Weekday = (typeof WEEKDAYS)[number];

const weeklySchema = z
  .object({
    sun: z.array(intervalSchema).default([]),
    mon: z.array(intervalSchema).default([]),
    tue: z.array(intervalSchema).default([]),
    wed: z.array(intervalSchema).default([]),
    thu: z.array(intervalSchema).default([]),
    fri: z.array(intervalSchema).default([]),
    sat: z.array(intervalSchema).default([]),
  })
  .default({ sun: [], mon: [], tue: [], wed: [], thu: [], fri: [], sat: [] });

const specialDaySchema = z.object({
  date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "use AAAA-MM-DD"),
  label: optionalText,
  closed: z.boolean().default(false),
  intervals: z.array(intervalSchema).default([]),
});

export const hoursSchema = z
  .object({
    timezone: z.string().default("America/Sao_Paulo"),
    /** auto = segue a grade de horários; open/closed = força o status manualmente. */
    mode: z.enum(["auto", "open", "closed"]).default("auto"),
    /** O que fazer quando a loja estiver fechada: bloquear pedidos ou aceitar agendamento. */
    whenClosed: z.enum(["block", "schedule"]).default("block"),
    /** Pausa temporária dos pedidos (ex.: muito movimento). Mostra a mensagem abaixo. */
    ordersPaused: z.boolean().default(false),
    pausedMessage: optionalText,
    weekly: weeklySchema,
    special: z.array(specialDaySchema).default([]),
  })
  .default({
    timezone: "America/Sao_Paulo",
    mode: "auto",
    whenClosed: "block",
    ordersPaused: false,
    pausedMessage: null,
    weekly: { sun: [], mon: [], tue: [], wed: [], thu: [], fri: [], sat: [] },
    special: [],
  });
export type Hours = z.infer<typeof hoursSchema>;

export const PAYMENT_METHODS = ["pix", "cash", "credit", "debit"] as const;
export type PaymentMethod = (typeof PAYMENT_METHODS)[number];

const addonSchema = z.object({
  key,
  name: z.string().trim().min(1).max(120),
  description: optionalText,
  /** Preço cobrado quando esta opção é paga. 0 = usa o "extraPrice" do grupo. */
  price: money.default(0),
  /** Sempre cobrado, não consome as escolhas grátis (ex.: Nutella dentro de acompanhamentos). */
  alwaysPaid: z.boolean().default(false),
  /** false = aparece como "Esgotado" e não pode ser escolhido. */
  available: z.boolean().default(true),
  /** false = não aparece no cardápio. */
  active: z.boolean().default(true),
});

const addonGroupSchema = z.object({
  key,
  name: z.string().trim().min(1).max(120),
  description: optionalText,
  /** Mínimo de escolhas (1 ou mais = obrigatório). */
  min: z.number().int().min(0).default(0),
  /** Máximo de escolhas (null = sem limite). */
  max: z.number().int().min(1).nullable().default(null),
  /** Quantas escolhas são grátis. As seguintes são cobradas. */
  free: z.number().int().min(0).default(0),
  /** Valor cobrado por escolha excedente quando a opção não tem preço próprio. */
  extraPrice: money.default(0),
  /** Quantas vezes a MESMA opção pode ser escolhida (1 = marcar/desmarcar). */
  maxPerOption: z.number().int().min(1).max(20).default(1),
  addons: z.array(addonSchema).default([]),
});

const ruleOverride = z.object({
  min: z.number().int().min(0).optional(),
  max: z.number().int().min(1).nullable().optional(),
  free: z.number().int().min(0).optional(),
});
export type RuleOverride = z.infer<typeof ruleOverride>;

const variantSchema = z.object({
  key,
  name: z.string().trim().min(1).max(80),
  description: optionalText,
  price: money,
  /** Preço "de" (riscado) para destacar promoção. */
  compareAtPrice: money.nullish().transform((v) => v ?? null),
  available: z.boolean().default(true),
  /** Regras específicas deste tamanho, por grupo. Ex.: { "acompanhamentos": { "free": 4 } } */
  rules: z.record(z.string(), ruleOverride).default({}),
});

const productGroupLink = z.union([
  key,
  z.object({ group: key }).extend(ruleOverride.shape),
]);

export const BADGES = ["mais-vendido", "promocao", "novo", "vegano", "zero-acucar", "destaque"] as const;

const productSchema = z.object({
  key,
  /** Copia todos os campos de outro produto e sobrescreve só o que for informado aqui. */
  extends: key.optional(),
  category: key.optional(),
  name: z.string().trim().min(1).max(120).optional(),
  description: optionalText.optional(),
  image: imageRef.optional(),
  /** Preço único, para produtos sem tamanhos. */
  price: money.nullish(),
  compareAtPrice: money.nullish(),
  variants: z.array(variantSchema).optional(),
  /** Nome exibido acima dos tamanhos (padrão: "Escolha o tamanho"). */
  variantLabel: optionalText.optional(),
  addonGroups: z.array(productGroupLink).optional(),
  badges: z.array(z.enum(BADGES)).optional(),
  featured: z.boolean().optional(),
  available: z.boolean().optional(),
  active: z.boolean().optional(),
});
export type ProductInput = z.infer<typeof productSchema>;

const categorySchema = z.object({
  key,
  name: z.string().trim().min(1).max(60),
  description: optionalText,
  icon: optionalText,
  active: z.boolean().default(true),
});

const zoneSchema = z.object({
  neighborhood: z.string().trim().min(1).max(120),
  fee: money,
  active: z.boolean().default(true),
});

export const storeConfigSchema = z
  .object({
    $schema: z.string().optional(),
    slug: key.max(60).refine((s) => !RESERVED_SLUGS.has(s), "slug reservado pelo sistema"),
    name: z.string().trim().min(1).max(120),
    /** Lojas de demonstração exibem um aviso "Demonstração" e nunca devem ser usadas para vendas reais. */
    isDemo: z.boolean().default(false),
    active: z.boolean().default(true),
    description: optionalText,
    seo: z
      .object({ title: optionalText, description: optionalText, image: imageRef })
      .default({ title: null, description: null, image: null }),
    branding: z.object({
      logo: imageRef,
      cover: imageRef,
      primaryColor: hexColor.default("#6B21A8"),
      secondaryColor: hexColor.default("#F59E0B"),
    }),
    banner: z
      .object({
        enabled: z.boolean().default(true),
        image: imageRef,
        title: optionalText,
        subtitle: optionalText,
      })
      .default({ enabled: false, image: null, title: null, subtitle: null }),
    contact: z.object({
      /** Somente dígitos com DDI 55 + DDD + número. Ex.: 5511987654321 */
      whatsapp: z.string().regex(/^\d{12,15}$/, "use apenas dígitos com DDI+DDD (ex.: 5511987654321)"),
      instagram: optionalText,
      address: optionalText,
      region: optionalText,
      mapsUrl: optionalText,
    }),
    hours: hoursSchema,
    ordering: z
      .object({
        delivery: z.boolean().default(true),
        pickup: z.boolean().default(true),
        minOrder: money.default(0),
        deliveryTime: optionalText,
        pickupTime: optionalText,
        paymentMethods: z.array(z.enum(PAYMENT_METHODS)).min(1).default(["pix", "cash", "credit", "debit"]),
        pixKey: optionalText,
      })
      .default({
        delivery: true,
        pickup: true,
        minOrder: 0,
        deliveryTime: null,
        pickupTime: null,
        paymentMethods: ["pix", "cash", "credit", "debit"],
        pixKey: null,
      }),
    delivery: z
      .object({
        /** fixed = taxa única · zones = taxa por bairro · free = entrega grátis */
        mode: z.enum(["fixed", "zones", "free"]).default("fixed"),
        fixedFee: money.default(0),
        /** Entrega grátis a partir deste subtotal (null = desativado). */
        freeAbove: money.nullish().transform((v) => v ?? null),
        /** Permitir bairros fora da lista (taxa "a combinar" com a loja). */
        allowUnlistedNeighborhoods: z.boolean().default(false),
        zones: z.array(zoneSchema).default([]),
      })
      .default({ mode: "fixed", fixedFee: 0, freeAbove: null, allowUnlistedNeighborhoods: false, zones: [] }),
    whatsappMessage: z
      .object({
        header: optionalText,
        footer: optionalText,
      })
      .default({ header: null, footer: null }),
    categories: z.array(categorySchema).default([]),
    addonGroups: z.array(addonGroupSchema).default([]),
    products: z.array(productSchema).default([]),
  })
  .superRefine((cfg, ctx) => {
    const dup = (list: string[], path: (string | number)[], what: string) => {
      const seen = new Set<string>();
      list.forEach((k, i) => {
        if (seen.has(k)) ctx.addIssue({ code: "custom", path: [...path, i, "key"], message: `${what} duplicado: "${k}"` });
        seen.add(k);
      });
    };
    dup(cfg.categories.map((c) => c.key), ["categories"], "categoria");
    dup(cfg.addonGroups.map((g) => g.key), ["addonGroups"], "grupo");
    dup(cfg.products.map((p) => p.key), ["products"], "produto");
    cfg.addonGroups.forEach((g, gi) => {
      dup(g.addons.map((a) => a.key), ["addonGroups", gi, "addons"], "opção");
      if (g.max !== null && g.min > g.max)
        ctx.addIssue({ code: "custom", path: ["addonGroups", gi, "min"], message: "min maior que max" });
    });
    if (cfg.delivery.mode === "zones" && cfg.ordering.delivery && cfg.delivery.zones.length === 0)
      ctx.addIssue({ code: "custom", path: ["delivery", "zones"], message: "modo 'zones' exige pelo menos um bairro" });
    if (!cfg.ordering.delivery && !cfg.ordering.pickup)
      ctx.addIssue({ code: "custom", path: ["ordering"], message: "ative entrega e/ou retirada" });
  });

export type StoreConfigInput = z.input<typeof storeConfigSchema>;
export type StoreConfig = z.output<typeof storeConfigSchema>;
