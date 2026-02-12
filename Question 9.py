import csv
import requests
from bs4 import BeautifulSoup
# Set the URL and send a request to get the webpage
url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {"User-Agent": "Mozilla/5.0"}  # Pretend to be a browser
response = requests.get(url, headers=headers)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# Find the main content area and all tables inside it
content_div = soup.find("div", id="mw-content-text")
all_tables = content_div.find_all("table")
# Find the first table that has at least 3 rows
target_table = None
for table in all_tables:
    rows = table.find_all("tr")
    if len(rows) >= 3:
        target_table = table
        break
# Process the table if we found one
if target_table:
    all_rows = target_table.find_all("tr")
    # Get column names from the first row
    first_row_cells = all_rows[0].find_all(["th", "td"])
    headers_list = []
    for cell in first_row_cells:
        headers_list.append(cell.get_text(strip=True))
    # If no headers found, create default column names
    if not headers_list:
        num_cols = len(first_row_cells)
        for i in range(num_cols):
            headers_list.append(f"col{i + 1}")
    # Prepare table data (rows)
    table_data = []
    # Start from the second row (actual data rows)
    for row in all_rows[1:]:
        cells = row.find_all(["td", "th"])
        row_content = []
        for cell in cells:
            row_content.append(cell.get_text(strip=True))
        # If a row has fewer columns, add empty strings
        while len(row_content) < len(headers_list):
            row_content.append("")
        table_data.append(row_content)
    # Save the table to a CSV file
