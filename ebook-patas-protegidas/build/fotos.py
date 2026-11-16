"""Gera os recortes das fotografias usadas no e-book.

As fotos originais ficam em imagens/fotos-originais/ e nunca são alteradas.
Os recortes são apenas enquadramentos (sem distorção, sem filtros que
mudem a aparência dos cães): leve ajuste de nitidez e exportação em JPEG.
"""
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
ORIG = RAIZ / "imagens" / "fotos-originais"
SAIDA = RAIZ / "imagens" / "fotos"
SAIDA.mkdir(parents=True, exist_ok=True)

# nome_saida: (arquivo_original, caixa_de_recorte ou None, largura_max)
RECORTES = {
    "caramelo-capa": ("foto2-caramelo-olhar.jpg", None, 1400),
    "caramelo-rosto": ("foto2-caramelo-olhar.jpg", (120, 200, 700, 780), 1200),
    "caramelo-meio": ("foto2-caramelo-olhar.jpg", (0, 180, 720, 1010), 1200),
    "pretocaramelo-inteiro": ("foto3-preto-caramelo-agua.jpg", None, 1200),
    "pretocaramelo-agua": ("foto3-preto-caramelo-agua.jpg", (0, 0, 675, 820), 1200),
    "pretocaramelo-rosto": ("foto3-preto-caramelo-agua.jpg", (110, 330, 590, 810), 1000),
    "dachshund-filhote": ("foto4-dachshund-filhote.jpg", None, 1200),
    "dachshund-filhote-rosto": ("foto4-dachshund-filhote.jpg", (40, 60, 700, 720), 1000),
    "dachshund-pelolongo": ("foto5-dachshund-pelo-longo.jpg", None, 1200),
    "dachshund-pelolongo-rosto": ("foto5-dachshund-pelo-longo.jpg", (70, 0, 700, 630), 1000),
    "filhotes-grupo": ("foto1-filhotes-dormindo.jpg", (130, 270, 736, 981), 1200),
    "filhotes-abraco": ("foto1-filhotes-dormindo.jpg", (190, 590, 736, 981), 1200),
    "filhote-sozinho": ("foto1-filhotes-dormindo.jpg", (40, 110, 390, 345), 900),
    "filhotes-inteiro": ("foto1-filhotes-dormindo.jpg", None, 1200),
}


def processar(nome, arquivo, caixa, largura_max):
    img = Image.open(ORIG / arquivo).convert("RGB")
    if caixa:
        img = img.crop(caixa)
    # amplia com qualidade quando a foto é pequena, para impressão mais suave
    w, h = img.size
    if w < largura_max:
        fator = min(largura_max / w, 2.0)
        img = img.resize((round(w * fator), round(h * fator)), Image.LANCZOS)
        img = img.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    img = ImageEnhance.Contrast(img).enhance(1.03)
    destino = SAIDA / f"{nome}.jpg"
    img.save(destino, "JPEG", quality=86, optimize=True, progressive=True)
    print(f"{destino.name}: {img.size}")


if __name__ == "__main__":
    for nome, (arq, caixa, lmax) in RECORTES.items():
        processar(nome, arq, caixa, lmax)
