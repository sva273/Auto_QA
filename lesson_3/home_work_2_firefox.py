from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


# Настройка драйвера для Firefox с использованием
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


# Изменение размера окна
driver.fullscreen_window()

# Открытие сайта
driver.get("https://itcareerhub.de/ru")

about_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
about_link.click()
# Задержка перед закрытием браузера
sleep(3
      )

# Сохранение скриншота
driver.save_screenshot("./itc_payment_screenshot_5.png") # Сохранение скриншота в текущую папку

sleep(3)
driver.quit()