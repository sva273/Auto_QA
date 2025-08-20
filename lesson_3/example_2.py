from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Инициализация драйвера
driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открытие страниц
driver.get("https://itcareerhub.de/ru/") # Открывается первая страница

driver.get("https://www.berlin.de") # Открывается вторая страница

# Задержка
sleep(5) # Скрипт "засыпает" на 5 секунд