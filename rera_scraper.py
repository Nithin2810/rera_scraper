import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://rera.odisha.gov.in"
PROJECT_LIST_URL = f"{BASE_URL}/projects/project-list"

response = requests.get(PROJECT_LIST_URL)
soup = BeautifulSoup(response.content, "html.parser")

# Find all "View Details" links
links = soup.find_all("a", string="View Details")
first_6_links = [BASE_URL + link['href'] for link in links[:6]]

project_data = []

for url in first_6_links:
    res = requests.get(url)
    detail_soup = BeautifulSoup(res.content, "html.parser")

    try:
        rera_no = detail_soup.find("span", id="lblRegistrationNumber").text.strip()
        project_name = detail_soup.find("span", id="lblProjectName").text.strip()
        promoter_name = detail_soup.find("span", id="lblPromoterName").text.strip()
        promoter_address = detail_soup.find("span", id="lblRegisteredAddress").text.strip()
        gst_no = detail_soup.find("span", id="lblGSTIN").text.strip()
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        continue

    project_data.append({
        "RERA Regd. No": rera_no,
        "Project Name": project_name,
        "Promoter Name": promoter_name,
        "Promoter Address": promoter_address,
        "GST No.": gst_no
    })

# Output the result as JSON
print(json.dumps(project_data, indent=2))
