import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_setup import setup_webdriver

def perform_login(driver, url):
    driver.get(url)
    input("Please login manually and press Enter to continue...")
    
    # handle this case as needed
    loggedin = driver.find_elements(By.XPATH, "//*[name()='path'][contains(@d,'m459.603 1077.948-1.762 2.851a.89.89 0 0 1-1.302.245l-1.402-1.072a.354.354')]")

    # Capture cookies if logged in
    if loggedin:
        cookies = driver.get_cookies()
        df = pd.DataFrame(cookies)
        df.to_excel("cookies.xlsx", index=False)
        print("Caught Cookie successfully.")

    else:
        print("Login failed or element not found, .")
