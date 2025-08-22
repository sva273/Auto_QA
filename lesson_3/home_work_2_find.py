from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Настройка ChromeDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Изменение размера окна
driver.fullscreen_window()


# Открытие сайта
driver.get("https://itcareerhub.de/ru")

about_link = driver.find_element(By.LINK_TEXT, "О нас")
about_link.click()
# Задержка перед закрытием браузера
sleep(10)

# Сохранение скриншота
driver.save_screenshot("./itc_payment_screenshot_3.png") # Сохранение скриншота в текущую папку