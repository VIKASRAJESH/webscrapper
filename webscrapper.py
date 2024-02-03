import requests
from bs4 import BeautifulSoup
import json
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# Fetch the website content
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the textual content from paragraphs
paragraphs = soup.find_all("p")
text_data = []
for paragraph in paragraphs:
    text = paragraph.get_text(separator=" ", strip=True)  # Clean and extract text
    if text:  # Skip empty paragraphs
        text_data.append(text)

# Save the extracted text in a JSON file
with open("extracted_text.json", "w") as file:
    json.dump(text_data, file, indent=4)

print("Textual information extracted and saved successfully!")
f = open("extracted_text.json", "r")
print(f.read())