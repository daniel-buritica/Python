from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def setting_options_argument():
    driver_path = ChromeDriverManager().install()
    exp_opt = [
        'enable-automation',
        'ignore-certification_errors',
        'enable-logging'
    ]
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "intl-accept_languages": ["es-ES", "es"],
        "credentials_enable_service": False

    }
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 "
                  "Safari/537.36")
    options = Options()
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-blink-feature=AutomationControlled")
    options.add_experimental_option("excludeSwitches", exp_opt)
    options.add_experimental_option("prefs", prefs)
    s = Service(driver_path)
    return webdriver.Chrome(service=s, options=options)


if __name__ == '__main__':
    url = "https://www.farmatodo.com.co/mundo-ofertas/49092"
    driver = setting_options_argument()
    driver.get(url)
    products = driver.find_elements(By.CSS_SELECTOR, "div.card-unique")

    for producto in products:
        title = producto.find_element(By.CSS_SELECTOR, "p.text-title").text
        print(title)



    driver.quit()
