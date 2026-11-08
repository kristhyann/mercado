from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
src,out=sys.argv[1],sys.argv[2]
F='/home/user/mercado/videos/_kit/node_modules/@fontsource/poppins/files/'
# converter woff2 -> ttf via fontTools
from fontTools.ttLib import TTFont
f=TTFont(F+'poppins-latin-900-normal.woff2'); f.flavor=None; f.save('/tmp/P900.ttf')
im=Image.open(src).convert('RGB')
W,H=im.size
# leve escurecimento embaixo para leitura
grad=Image.new('L',(W,H),0); g=ImageDraw.Draw(grad)
for y in range(H): g.line([(0,y),(W,y)],fill=int(max(0,(y-1050)/(H-1050))*150))
im=Image.composite(Image.new('RGB',(W,H),(0,0,0)),im,grad)
d=ImageDraw.Draw(im)
def text(t,y,size,fill,stroke=18):
    fo=ImageFont.truetype('/tmp/P900.ttf',size)
    w=d.textlength(t,font=fo)
    # sombra
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).text(((W-w)/2,y+14),t,font=fo,fill=(0,0,0,140),stroke_width=stroke,stroke_fill=(0,0,0,140))
    im.paste(sh.filter(ImageFilter.GaussianBlur(4)),(0,0),sh.filter(ImageFilter.GaussianBlur(4)))
    ImageDraw.Draw(im).text(((W-w)/2,y),t,font=fo,fill=fill,stroke_width=stroke,stroke_fill=(17,17,17))
text('VOCÊ É UM',1180,150,(255,255,255))
text('PREGO',1330,270,(255,138,31),22)
im.save(out,quality=92)
