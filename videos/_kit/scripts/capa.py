# uso: python3 capa.py quadro.png saida.jpg "LINHA 1" "LINHA 2"   (sempre com a marca @olhaso_3D)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys, os
src, out, l1, l2 = sys.argv[1:5]
TTF = '/tmp/claude-0/P900.ttf'
if not os.path.exists(TTF):
    from fontTools.ttLib import TTFont
    f = TTFont(os.path.join(os.path.dirname(__file__), '../node_modules/@fontsource/poppins/files/poppins-latin-900-normal.woff2')); f.flavor = None; f.save(TTF)
im = Image.open(src).convert('RGB'); W, H = im.size
grad = Image.new('L', (W, H), 0); g = ImageDraw.Draw(grad)
for y in range(H): g.line([(0, y), (W, y)], fill=int(max(0, (y - 1050) / (H - 1050)) * 150))
im = Image.composite(Image.new('RGB', (W, H), (0, 0, 0)), im, grad)
def text(t, y, size, fill, stroke=18):
    fo = ImageFont.truetype(TTF, size); d = ImageDraw.Draw(im)
    while d.textlength(t, font=fo) > W - 80 and size > 60: size -= 6; fo = ImageFont.truetype(TTF, size)
    w = d.textlength(t, font=fo)
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).text(((W - w) / 2, y + 14), t, font=fo, fill=(0, 0, 0, 140), stroke_width=stroke, stroke_fill=(0, 0, 0, 140))
    sh = sh.filter(ImageFilter.GaussianBlur(4)); im.paste(sh, (0, 0), sh)
    ImageDraw.Draw(im).text(((W - w) / 2, y), t, font=fo, fill=fill, stroke_width=stroke, stroke_fill=(17, 17, 17))
text(l1, 1250, 130, (255, 255, 255), 14)
text(l2, 1390, 260, (255, 138, 31), 22)
ImageDraw.Draw(im).text((44, 70), '@olhaso_3D', font=ImageFont.truetype(TTF, 52), fill=(255, 255, 255), stroke_width=7, stroke_fill=(17, 17, 17))
im.save(out, quality=92)
