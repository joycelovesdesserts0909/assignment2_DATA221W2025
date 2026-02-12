import csv
import requests
from bs4 import BeautifulSoup

# Bước 1: Thiết lập URL và lấy dữ liệu web [cite: 123, 124]
url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Bước 2: Tìm vùng nội dung chính và tất cả các bảng [cite: 125]
content_div = soup.find("div", id="mw-content-text")
all_tables = content_div.find_all("table")

# Bước 3: Tìm bảng đầu tiên có ít nhất 3 hàng [cite: 125]
target_table = None
for table in all_tables:
    rows = table.find_all("tr")
    if len(rows) >= 3:
        target_table = table
        break

# Bước 4: Xử lý bảng nếu tìm thấy [cite: 126, 127, 128]
if target_table:
    all_rows = target_table.find_all("tr")

    # Lấy tiêu đề từ hàng đầu tiên (thẻ <th>)
    first_row_cells = all_rows[0].find_all(["th", "td"])
    headers_list = []
    for cell in first_row_cells:
        headers_list.append(cell.get_text(strip=True))

    # Nếu không tìm thấy header, tạo tên mặc định col1, col2...
    if not headers_list:
        num_cols = len(first_row_cells)
        for i in range(num_cols):
            headers_list.append(f"col{i + 1}")

    # Chuẩn bị dữ liệu để lưu [cite: 127]
    table_data = []
    # Duyệt từ hàng thứ 2 trở đi (dữ liệu thực tế)
    for row in all_rows[1:]:
        cells = row.find_all(["td", "th"])
        row_content = []
        for cell in cells:
            row_content.append(cell.get_text(strip=True))

        # Đệm thêm chuỗi rỗng nếu hàng thiếu cột [cite: 127]
        while len(row_content) < len(headers_list):
            row_content.append("")

        table_data.append(row_content)

    # Bước 5: Ghi dữ liệu vào file CSV
    with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers_list)  # Ghi hàng tiêu đề
        writer.writerows(table_data)  # Ghi tất cả các hàng dữ liệu

    print("Successfully saved table to wiki_table.csv")