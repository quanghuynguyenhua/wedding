"""Nén ảnh gốc cho album. Cần: pip install pillow
Dùng:  python tools/prepare_photos.py thu-muc-anh-goc san-truong
Ảnh nén được ghi vào album/img/full và album/img/thumbs, rồi in danh sách để dán vào PHOTOS trong album/index.html."""
import sys, json, os
from PIL import Image, ImageOps
src, album = sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "album"
root = os.path.join(os.path.dirname(__file__), "..", "album", "img")
for d in ("full", "thumbs"): os.makedirs(os.path.join(root, d), exist_ok=True)
out = []
for n in sorted(os.listdir(src)):
    if not n.lower().endswith((".jpg", ".jpeg", ".png")): continue
    im = ImageOps.exif_transpose(Image.open(os.path.join(src, n))).convert("RGB")
    f = os.path.splitext(n)[0].lower().replace(" ", "-") + ".jpg"
    big = im.copy(); big.thumbnail((1800, 1800)); big.save(os.path.join(root, "full", f), "JPEG", quality=78, optimize=True, progressive=True)
    t = im.copy(); t.thumbnail((640, 640)); t.save(os.path.join(root, "thumbs", f), "JPEG", quality=70, optimize=True, progressive=True)
    out.append({"f": f, "a": album, "c": "", "w": t.width, "h": t.height})
print(json.dumps(out, ensure_ascii=False, indent=1))
