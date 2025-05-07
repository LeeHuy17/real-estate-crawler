# Real Estate Crawler

Dự án Python tự động thu thập dữ liệu nhà đất cho thuê từ trang [alonhadat.com.vn](https://alonhadat.com.vn).

## Tính năng

- Lấy dữ liệu bất động sản cho thuê tại Đà Nẵng.
- Lưu dữ liệu ra file Excel (.xlsx).
- Tự động chạy mỗi ngày lúc 06:00 sáng.
- Có thể mở rộng cho nhiều tỉnh thành khác.

## Yêu cầu hệ thống

- Python 3.8 hoặc mới hơn
- Google Chrome
- ChromeDriver (cùng version với Chrome)
- Thư viện: selenium, pandas, openpyxl

## Cài đặt

```bash
git clone https://github.com/LeeHuy17/real-estate-crawler.git
cd real-estate-crawler
pip install -r requirements.txt
