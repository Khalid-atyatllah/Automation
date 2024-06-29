from selenium import webdriver
from chrome_options import get_chrome_options

def setup_webdriver():
    chrome_options = get_chrome_options()
    driver = webdriver.Chrome(options=chrome_options)
    return driver
