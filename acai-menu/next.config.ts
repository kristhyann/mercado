import type { NextConfig } from "next";

const remotePatterns: NonNullable<NonNullable<NextConfig["images"]>["remotePatterns"]> = [];

// Libera otimização de imagens do Supabase Storage do projeto configurado.
if (process.env.SUPABASE_URL) {
  try {
    const { hostname } = new URL(process.env.SUPABASE_URL);
    remotePatterns.push({ protocol: "https", hostname, pathname: "/storage/v1/object/public/**" });
  } catch {
    // URL inválida: ignorada aqui, o app avisa no log em tempo de execução.
  }
}

const nextConfig: NextConfig = {
  reactStrictMode: true,
  poweredByHeader: false,
  // Inclui os arquivos das lojas locais (demonstração) no deploy da Vercel.
  outputFileTracingIncludes: { "/**": ["./stores/**/*"] },
  images: {
    remotePatterns,
    formats: ["image/avif", "image/webp"],
    deviceSizes: [360, 414, 640, 768, 1024, 1280],
    minimumCacheTTL: 3600,
  },
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          { key: "X-Frame-Options", value: "SAMEORIGIN" },
          { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
        ],
      },
    ];
  },
};

export default nextConfig;
