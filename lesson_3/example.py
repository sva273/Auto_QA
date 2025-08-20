from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Укажите путь к драйверу (файл chromedriver, а не папка)
driver_path = "/Users/aaaaaaaaa/Downloads/chromedriver-mac-arm64/chromedriver"

# Создание сервиса для драйвера
service = Service(driver_path)

# Инициализация драйвера с использованием сервиса
driver = webdriver.Chrome(service=service)

# Открытие сайта
driver.get("https://itcareerhub.de/ru")

# Задержка перед закрытием браузера
sleep(50)
