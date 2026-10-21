# Huy & Trang — A journey of love

Website đám cưới · 29.12.2026 · Lotte Hotel Saigon

## Thêm ảnh (không cần sửa code)

1. Kéo ảnh vào đúng folder trong `assets/photos/` (bảng dưới).
2. GitHub Desktop → **Commit** → **Push origin**.
3. Khoảng 2–3 phút sau trang tự cập nhật. Ảnh trên 2 MB được tự động nén.

Thứ tự ảnh theo tên file (A→Z). Muốn tấm nào lên trước thì đặt tên `01_...`, `02_...`.

| Folder | Hiện ở đâu |
|---|---|
| `journey/calgary`, `montreal`, `toronto`, `belgium`, `korea`, `taiwan`, `philippines`, `thailand`, `vietnam`, `singapore` | Bấm vào nơi đó trên địa cầu |
| `journey/cats` | Bấm vào tên lửa (Danou & Bébé) |
| `prewedding` | Photos → Ảnh cưới (ảnh mới tự nối vào cuối) |
| `civil` | Photos → Lễ đăng ký kết hôn |
| `family/bw`, `bride-groom`, `family-friends`, `details` | Photos → Lễ gia tiên (lọc bằng dấu +) |
| `wedding/bw`, `bride-groom`, `guests`, `details`, `more` | Photos → Tiệc cưới (lọc bằng dấu +) |
| `frontpage` | Ảnh mở đầu + clip cuối Intro (cố định, đổi thì nhờ sửa code) |

File `.gitkeep` trong folder trống chỉ để Git giữ folder, cứ để đó.
Định dạng nhận: .jpg .jpeg .png .webp (ảnh HEIC của iPhone thì xuất sang JPG trước). Mỗi file phải dưới 100 MB (giới hạn của GitHub).

## Lần đầu đưa lên GitHub Pages

1. Copy toàn bộ nội dung folder này (kể cả folder ẩn `.github`) vào `C:\Users\admin\Documents\GitHub\wedding`.
2. Commit + Push lên nhánh `main`.
3. Trên GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Tab **Actions** sẽ chạy "Build & deploy site"; xong thì trang ở `https://<tên-github>.github.io/wedding/`.

## Cấu trúc

```
index.html                     toàn bộ trang
assets/photos/…                ảnh (xem bảng trên)
assets/music/part0–2.mp4       nhạc nền
scripts/build_photos.py        nén ảnh > 2 MB + tạo assets/photos/photos.json (chạy trên GitHub)
.github/workflows/deploy.yml   tự build và đưa trang lên GitHub Pages mỗi lần push
```
