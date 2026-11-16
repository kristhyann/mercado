import type { MetadataRoute } from "next";
import { listStoreSlugs } from "@/lib/data";
import { env } from "@/lib/env";

export const revalidate = 3600;

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const stores = await listStoreSlugs();
  return [
    { url: env.siteUrl, changeFrequency: "monthly", priority: 0.5 },
    ...stores.map((s) => ({ url: `${env.siteUrl}/${s.slug}`, lastModified: s.updatedAt ?? undefined, changeFrequency: "daily" as const, priority: 1 })),
  ];
}
