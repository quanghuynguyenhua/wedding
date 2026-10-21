"""Prepare the site for GitHub Pages.

Runs in GitHub Actions on every push (see .github/workflows/deploy.yml):
  1. every photo larger than 2 MB under assets/photos is resized (longest side 2000 px)
     and saved as .webp; the original is replaced in the deployed copy only
     (the repository itself keeps what you pushed);
  2. assets/photos/photos.json lists the photos of every folder, sorted by file name.

Usage: python scripts/build_photos.py <site-folder>
"""
import json, os, sys
from PIL import Image, ImageOps

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
PHOTOS = os.path.join(ROOT, "assets", "photos")
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
LIMIT = 2 * 1024 * 1024
SKIP = {"frontpage"}            # fixed images used by the intro, listed in index.html

Image.MAX_IMAGE_PIXELS = None


def shrink(path):
    stem, _ = os.path.splitext(path)
    out = stem + ".webp"
    im = Image.open(path)
    im.draft("RGB", (4000, 4000))
    im = ImageOps.exif_transpose(im).convert("RGB")
    im.thumbnail((2000, 2000), Image.LANCZOS)
    im.save(out, "WEBP", quality=80, method=5)
    if out != path:
        os.remove(path)
    print(f"compressed {os.path.relpath(path, ROOT)} -> {os.path.relpath(out, ROOT)} "
          f"({os.path.getsize(out) // 1024} KB)")
    return out


manifest = {}
for dirpath, dirnames, filenames in os.walk(PHOTOS):
    dirnames.sort()
    rel = os.path.relpath(dirpath, PHOTOS).replace(os.sep, "/")
    if rel.split("/")[0] in SKIP:
        continue
    files = []
    for name in sorted(filenames, key=str.lower):
        p = os.path.join(dirpath, name)
        if os.path.splitext(name)[1].lower() not in EXTS:
            continue
        if os.path.getsize(p) > LIMIT:
            p = shrink(p)
        files.append(os.path.relpath(p, ROOT).replace(os.sep, "/"))
    if rel != "." and (files or not dirnames):
        manifest[rel] = files

with open(os.path.join(PHOTOS, "photos.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=1)
print("photos.json:", {k: len(v) for k, v in manifest.items()})
