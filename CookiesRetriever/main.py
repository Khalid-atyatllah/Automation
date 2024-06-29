from webdriver_setup import setup_webdriver
from login_process import perform_login
from cleanup import cleanup

if __name__ == "__main__":
    url = "https://www.example.com"  # Replace with your desired URL
    
    try:
        driver = setup_webdriver()
        perform_login(driver, url)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        cleanup(driver)
