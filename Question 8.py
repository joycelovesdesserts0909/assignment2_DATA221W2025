import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Data_science"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
content_div = soup.find("div", id="mw-content-text")
# List of headings we do NOT want to include
exclude_list = ["References", "External links", "See also", "Notes"]
# Find all <h2> headings inside the main content
headings = content_div.find_all("h2")
# Open file to write the results
with open("headings.txt", "w", encoding="utf-8") as f:
    # Go through each heading one by one
    for h in headings:
        # Get the text inside the <h2> tag
        text = h.get_text()
        # Remove the "[edit]" part
        text = text.replace("[edit]", "")
        # Remove extra spaces
        text = text.strip()
        # Assume we will keep this heading
        keep_heading = True
        # Check if the heading contains any unwanted words
        for word in exclude_list:
            if word in text:
                keep_heading = False
        # If it does NOT contain unwanted words, write it to the file
        if keep_heading:
            f.write(text + "\n")
