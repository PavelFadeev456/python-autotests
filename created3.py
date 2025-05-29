from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login():
    options = Options()
    driver_path = r"D:\Windows\drivers\chromedriver-win64\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)

    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        print("✅ Login test passed")

    except Exception as e:
        print(f"❌ Login test failed: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_valid_login()



