from PIL import Image, ImageDraw, ImageFont
import os, sys
R='/home/claude/stethos-repo/public'
W,H=1200,630
bg=Image.new('RGB',(W,H),(208,210,249))
art=Image.open(R+'/img/g-hero-3200.webp').convert('RGB')
s=1320/art.width; a=art.resize((1320,round(art.height*s)),Image.LANCZOS)
mask=Image.new('L',a.size,255); md=ImageDraw.Draw(mask); fade=120
for y in range(fade): md.line([(0,y),(a.width,y)],fill=int(255*(y/fade)**1.5))
top=H-a.height+110
bg.paste(a,(-60,top),mask)
d=ImageDraw.Draw(bg)
h1=ImageFont.truetype('/tmp/fl/figtree650.ttf',66)
sub=ImageFont.truetype('/tmp/fl/figtree500.ttf',29)
brand=ImageFont.truetype('/tmp/fl/figtree650.ttf',36)
logo=Image.open(R+'/img/g-cl-logo-cut.webp').convert('RGBA').resize((60,60),Image.LANCZOS)
bw=60+10+d.textlength('Stethos',font=brand); bx=(W-bw)/2
bg.paste(logo,(int(bx),26),logo); d.text((bx+70,34),'Stethos',font=brand,fill=(0,0,0))
for i,t in enumerate(['Healthcare data','for your AI agents']):
    tw=d.textlength(t,font=h1); d.text(((W-tw)/2,104+i*72),t,font=h1,fill=(0,0,0))
bg.save(sys.argv[1],quality=86,optimize=True,progressive=True)
print(top, a.height, os.path.getsize(sys.argv[1]))
bg.crop(((W-H)//2,0,(W+H)//2,H)).resize((300,300)).save('/tmp/fl/og_sq.png')
