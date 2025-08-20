from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Настройка ChromeDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Открытие сайта
driver.get("https://itcareerhub.de/ru")

# Задержка перед закрытием браузера
sleep(5)
