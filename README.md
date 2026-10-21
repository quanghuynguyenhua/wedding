# Huy & Trang — A journey of love

Website đám cưới · 29.12.2026 · Lotte Hotel Saigon

## Cấu trúc

```
index.html                  toàn bộ trang (HTML + CSS + JS)
assets/
  photos/
    frontpage/              ảnh mở đầu + clip ảnh cuối Intro
    prewedding/             ảnh Pre-wedding (đã nén)
    journey/belgium/        ảnh từng nơi trong Journey (mỗi nơi một folder)
    cats/                   ảnh Danou & Bébé
  music/                    nhạc nền, chia 3 đoạn (part0–2.mp4)
.nojekyll                   để GitHub Pages phục vụ file nguyên trạng
```

## Đưa lên GitHub Pages

1. Copy toàn bộ nội dung folder này vào `C:\Users\admin\Documents\GitHub\wedding`.
2. Commit + push lên nhánh `main`.
3. Trên GitHub: Settings → Pages → Source: Deploy from a branch → `main` / `(root)` → Save.
4. Vài phút sau trang chạy ở `https://<tên-github>.github.io/wedding/`.

## Thêm ảnh

Ảnh trên 2MB nên nén trước (khoảng 1600px cạnh dài). Bỏ ảnh mới vào đúng folder trong `assets/photos/`
rồi khai báo đường dẫn trong `index.html` (tìm `CITIES` cho Journey, `ALBUMS` cho Family Ceremony / Wedding).
