"""Prepare the site for GitHub Pages.

Runs in GitHub Actions on every push (see .github/workflows/deploy.yml):
  1. every photo larger than 2 MB under assets/photos is resized (longest side 2000 px)
     and saved as .webp; the original is replaced in the deployed copy only
     (the repository itself keeps what you pushed);
  2. video clips (.mp4 .mov .m4v .webm) are converted to small, silent H.264 .mp4 so every browser plays them;
  3. assets/photos/photos.json lists the photos of every folder, sorted by file name.

Usage: python scripts/build_photos.py <site-folder>
"""
import json, os, shutil, subprocess, sys
from PIL import Image, ImageOps

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
PHOTOS = os.path.join(ROOT, "assets", "photos")
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
VEXTS = {".mp4", ".mov", ".m4v", ".webm"}
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


def clip(path):
    """iPhone .mov/.mp4 (often HEVC) -> small H.264 .mp4 that every browser plays; muted, max 1280px."""
    stem, ext = os.path.splitext(path)
    out = stem + ".mp4"
    if not shutil.which("ffmpeg"):
        print("ffmpeg not found: keeping", os.path.relpath(path, ROOT), "as is")
        return path
    tmp = stem + ".web.mp4"
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", path,
                        "-vf", "scale='if(gt(iw,ih),min(1280,iw),-2)':'if(gt(iw,ih),-2,min(1280,ih))'",
                        "-c:v", "libx264", "-preset", "medium", "-crf", "27", "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart", "-an", tmp])
    if r.returncode != 0:
        print("could not convert", path, "- keeping it as is")
        if os.path.exists(tmp):
            os.remove(tmp)
        return path
    os.remove(path)
    os.replace(tmp, out)
    print(f"clip {os.path.relpath(path, ROOT)} -> {os.path.relpath(out, ROOT)} ({os.path.getsize(out) // 1024} KB)")
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
        ext = os.path.splitext(name)[1].lower()
        if ext in VEXTS:
            stem = os.path.splitext(name)[0]
            if ext != ".mp4" and stem + ".mp4" in filenames:
                continue        # already converted copy sits next to it
            p = clip(p) if ext != ".mp4" or os.path.getsize(p) > 25 * 1024 * 1024 else p
            if p:
                files.append(os.path.relpath(p, ROOT).replace(os.sep, "/"))
            continue
        if ext not in EXTS:
            continue
        if os.path.getsize(p) > LIMIT:
            p = shrink(p)
        files.append(os.path.relpath(p, ROOT).replace(os.sep, "/"))
    if rel != "." and (files or not dirnames):
        manifest[rel] = files

with open(os.path.join(PHOTOS, "photos.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=1)
print("photos.json:", {k: len(v) for k, v in manifest.items()})
