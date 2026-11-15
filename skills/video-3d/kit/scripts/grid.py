from PIL import Image;import glob,sys
fs=sorted(glob.glob(sys.argv[1]+'/*.jpg'));cols=int(sys.argv[3]) if len(sys.argv)>3 else 7;w,h=270,480
rows=(len(fs)+cols-1)//cols;g=Image.new('RGB',(w*cols,h*rows),'white')
for i,f in enumerate(fs): g.paste(Image.open(f).resize((w,h)),((i%cols)*w,(i//cols)*h))
g.save(sys.argv[2],quality=85)
