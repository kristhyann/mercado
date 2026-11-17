import Image, { type ImageProps } from "next/image";

/** next/image com tratamento para SVG (ilustrações de demonstração) e imagens externas. */
export function Img(props: ImageProps) {
  const src = typeof props.src === "string" ? props.src : "";
  const unoptimized = props.unoptimized ?? (src.endsWith(".svg") || src.startsWith("data:"));
  return <Image {...props} unoptimized={unoptimized} />;
}
