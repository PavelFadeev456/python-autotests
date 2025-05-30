from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time
import traceback

PAGES = [
    "https://only.digital/",
    "https://only.digital/projects",
    "https://only.digital/company",
    "https://only.digital/fields",
    "https://only.digital/job",
    "https://only.digital/blog",
    "https://only.digital/contacts"
]

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
    service = Service()
    return webdriver.Chrome(service=service, options=options)

def check_footer_elements(driver, url):
    print(f"\n Проверка страницы: {url}")
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
        footer = driver.find_element(By.TAG_NAME, "footer")
        print("Футер найден")

        # Логотип
        try:
            footer.find_element(By.CSS_SELECTOR, "img, svg")
            print("Логотип/иконка найдены")
        except NoSuchElementException:
            print("Логотип не найден")

        # Контакты
        try:
            contact = footer.find_element(By.XPATH, ".//*[contains(text(), '@') or contains(text(), '+')]")
            print(f"Контактная информация найдена: {contact.text}")
        except NoSuchElementException:
            print("Контактная информация не найдена")

        # Ссылки
        links = footer.find_elements(By.TAG_NAME, "a")
        print(f"Найдено ссылок в футере: {len(links)}" if links else "Ссылки не найдены")

    except Exception as e:
        print(f"Ошибка при проверке {url}: {str(e)}")
        traceback.print_exc()

def main():
    for page in PAGES:
        try:
            driver = init_driver()
            check_footer_elements(driver, page)
            time.sleep(2)
            driver.quit()
        except WebDriverException as e:
            print(f"Ошибка драйвера при проверке {page}: {e}")
            traceback.print_exc()

    print("\n Проверка завершена")

if __name__ == "__main__":
    main()



