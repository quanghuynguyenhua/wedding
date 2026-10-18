# Trang báo hỷ Quang Huy & Thanh Trang

- `index.html`: trang thiệp. Ảnh nằm trong `img/`.
- `album/index.html`: thư viện ảnh (sau đám cưới). Địa chỉ: `/album`.
- Hiện nút "Xem ảnh cưới" trên trang thiệp: mở `index.html`, tìm `SHOW_ALBUM=false`, đổi thành `true`.
- Thêm ảnh: `python tools/prepare_photos.py <thu-muc-anh-goc> <ma-album>`, dán danh sách in ra vào `PHOTOS` trong `album/index.html`, thêm tên album vào `ALBUMS` nếu là album mới, rồi đẩy lên GitHub.
- Bật Pages: GitHub repo, Settings, Pages, chọn nhánh chính và thư mục chứa `index.html`.
