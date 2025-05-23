from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize browser
browser = webdriver.Chrome()
browser.get("https://rera.odisha.gov.in/projects/project-list")
wait = WebDriverWait(browser, 10)

# Wait for "View Details" links to be loaded
wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"View Details")]')))
time.sleep(2)

# Fetch first 6 project links
project_links = browser.find_elements(By.XPATH, '//a[contains(text(),"View Details")]')[:6]

for index, _ in enumerate(project_links):
    # Refresh clickable links each time (DOM reloads after back)
    refreshed_links = browser.find_elements(By.XPATH, '//a[contains(text(),"View Details")]')
    browser.execute_script("arguments[0].click();", refreshed_links[index])
    print(f"\n--- Project {index + 1} ---")

    # Wait for detail block
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "details-project")))
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Extract project details
    detail_blocks = browser.find_elements(By.CLASS_NAME, "details-project")
    for section in detail_blocks:
        try:
            label_text = section.find_element(By.TAG_NAME, "label").text.strip()
            value_text = section.find_element(By.TAG_NAME, "strong").text.strip()
            if label_text in ["Project Name", "RERA Regd. No."]:
                print(f"{label_text}: {value_text}")
        except:
            continue

    # Switch to Promoter Details tab
    try:
        promoter_tab = browser.find_element(By.LINK_TEXT, "Promoter Details")
        browser.execute_script("arguments[0].click();", promoter_tab)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ms-3")))
        time.sleep(1)

        promoter_info = browser.find_elements(By.CLASS_NAME, "ms-3")
        for info in promoter_info:
            try:
                label_text = info.find_element(By.TAG_NAME, "label").text.strip()
                value_text = info.find_element(By.TAG_NAME, "strong").text.strip()
                if label_text in ["Company Name", "Registered Office Address", "GST No."]:
                    print(f"{label_text}: {value_text}")
            except:
                continue
    except Exception as error:
        print("Promoter tab issue or data not found:", error)

    # Go back to the list
    browser.back()
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"View Details")]')))
    time.sleep(2)

browser.quit()
