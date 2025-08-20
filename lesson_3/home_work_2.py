from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Настройка ChromeDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Изменение размера окна
driver.fullscreen_window()


# Открытие сайта
driver.get("https://itcareerhub.de/ru#rec717852307")

# Задержка перед закрытием браузера
sleep(10)

# Сохранение скриншота
driver.save_screenshot("./itc_payment_screenshot.png") # Сохранение скриншота в текущую папку
