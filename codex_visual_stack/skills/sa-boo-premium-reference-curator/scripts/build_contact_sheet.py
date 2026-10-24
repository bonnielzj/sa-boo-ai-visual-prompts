#!/usr/bin/env python3
"""Build a quick contact sheet from image files in a folder.
Usage: python build_contact_sheet.py /path/to/images_or_folder /path/to/output.jpg [--cols 5]
"""
from __future__ import annotations
from pathlib import Path
import sys, math, argparse
from PIL import Image, ImageOps, ImageDraw

EXTS={'.jpg','.jpeg','.png','.webp','.gif','.tif','.tiff'}

def image_paths(folder: Path):
    if (folder/'images').is_dir():
        folder=folder/'images'
    return sorted([p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in EXTS])

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('input')
    ap.add_argument('output')
    ap.add_argument('--cols',type=int,default=5)
    ap.add_argument('--tile-w',type=int,default=320)
    ap.add_argument('--tile-h',type=int,default=380)
    args=ap.parse_args()
    inp=Path(args.input).expanduser().resolve(); out=Path(args.output).expanduser().resolve()
    paths=image_paths(inp)
    if not paths: raise SystemExit(f'No images found under {inp}')
    cols=max(1,args.cols); tile=(args.tile_w,args.tile_h); label_h=54
    rows=math.ceil(len(paths)/cols)
    sheet=Image.new('RGB',(cols*tile[0],rows*tile[1]),(242,242,242))
    for i,p in enumerate(paths):
        can=Image.new('RGB',tile,(248,248,248))
        try:
            im=Image.open(p); im=ImageOps.exif_transpose(im).convert('RGB')
            im.thumbnail((tile[0]-20,tile[1]-label_h-16),Image.Resampling.LANCZOS)
            can.paste(im,((tile[0]-im.width)//2,8))
        except Exception:
            pass
        d=ImageDraw.Draw(can); y=tile[1]-label_h+8
        d.text((8,y),f'{i+1:03d}',fill=(0,0,0))
        d.text((54,y),p.name[:34],fill=(40,40,40))
        sheet.paste(can,((i%cols)*tile[0],(i//cols)*tile[1]))
    out.parent.mkdir(parents=True,exist_ok=True)
    sheet.save(out,quality=92,optimize=True)
    print(out)

if __name__=='__main__': main()
