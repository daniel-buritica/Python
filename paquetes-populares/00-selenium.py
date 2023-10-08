from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

driver_path = ChromeDriverManager().install()

s = Service(driver_path)
hots_farma = "https://www.farmatodo.com.co/mundo-ofertas/49092"
driver = webdriver.Chrome(service=s)

driver.get(hots_farma)
print(driver.page_source)

soup = BeautifulSoup(driver.page_source, "html.parser")