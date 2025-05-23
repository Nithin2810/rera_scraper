RERA Odisha Projects Scraper

Overview

This Python script scrapes the first 6 projects listed under the "Projects Registered" section on the RERA Odisha website.
It collects the following details for each project:

Rera Regd. No

Project Name

Promoter Name (Company Name)

Address of the Promoter (Registered Office Address)

GST No.



---

Requirements

Python 3.x

Libraries: requests, beautifulsoup4


Install dependencies using:

pip install requests beautifulsoup4


---

How to run

1. Clone the repository or download the script.


2. Run the script using Python 3:



python rera_scraper.py

3. The script outputs the details of the first 6 projects on the console.




---

Notes

The scraper uses HTTP requests and parses HTML content with BeautifulSoup.

If the website structure changes, the scraper may need adjustments.

The script does not use Selenium and assumes no login or captcha is required.



---

Contact

For any questions, contact:
Your Name – sarveshsatti@gmail.com
