from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# Настройка драйвера для Firefox с использованием
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


# Изменение размера окна
driver.fullscreen_window()


# Открытие сайта
driver.get("https://itcareerhub.de/ru#rec717852307")

# Задержка перед закрытием браузера


# Сохранение скриншота
driver.save_screenshot("./itc_payment_screenshot_2.png") # Сохранение скриншота в текущую папку

sleep(3)
driver.quit()