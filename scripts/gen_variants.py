import os,sys,glob
from PIL import Image
D=sys.argv[1]
TOUR_W=[400,800]
GAL_W=[160,480,960]
Q=82
def save(im,w,dst):
    if os.path.exists(dst): 
        return 0,False
    r=w/im.width
    nim=im.resize((w,max(1,round(im.height*r))), Image.LANCZOS)
    nim.save(dst,"WEBP",quality=Q,method=6)
    return os.path.getsize(dst),True
def variants(src,widths):
    im=Image.open(src).convert("RGB")
    base=src[:-5]  # strip .webp
    made=0; tot=0
    for w in widths:
        if w>=im.width: continue
        n,ok=save(im,w,f"{base}-{w}.webp")
        if ok: made+=1; tot+=n
    return made,tot
tot_made=0; tot_bytes=0
# tours (cards)
for f in sorted(glob.glob(os.path.join(D,"assets/img/tours/*.webp"))):
    if any(f.endswith(f"-{w}.webp") for w in TOUR_W): continue
    m,b=variants(f,TOUR_W); tot_made+=m; tot_bytes+=b
# gallery
for f in sorted(glob.glob(os.path.join(D,"assets/img/gallery/*/*.webp"))):
    bn=os.path.basename(f)
    if any(bn.endswith(f"-{w}.webp") for w in GAL_W): continue
    m,b=variants(f,GAL_W); tot_made+=m; tot_bytes+=b
# logo downscale in place -> 300px (RGBA preserved)
lg=os.path.join(D,"assets/img/logo.png")
im=Image.open(lg)
if im.width>300:
    im2=im.resize((300,round(im.height*300/im.width)), Image.LANCZOS)
    im2.save(lg,"PNG",optimize=True)
    print("logo.png ->",im2.size, os.path.getsize(lg)//1024,"KB")
print(f"variants made: {tot_made}, new bytes: {tot_bytes//1024} KB")
