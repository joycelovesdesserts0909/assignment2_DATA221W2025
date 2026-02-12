import requests
from bs4 import BeautifulSoup
# Send a request to the Wikipedia page
url = "https://en.wikipedia.org/wiki/Data_science"
# Add headers to mimic a real browser
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")
# Extract and print the page title from the <title> tag
if soup.title:
    page_title = soup.title.get_text().strip()
    print(f"Page Title: {page_title}")
else:
    print("No title found.")
# Extract the first paragraph from the main article content (mw-content-text)
content_div = soup.find("div", {"id": "mw-content-text"})
paragraphs = content_div.find_all("p")
for p in paragraphs:
    text = p.get_text().strip()
    # Only keep paragraphs with at least 50 characters
    if len(text) >= 50:
        print("\nFirst Paragraph (min 50 chars):")
        print(text)
        break
