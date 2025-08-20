from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Инициализация драйвера
driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.set_window_size(640, 460) # Устанавливаем размер окна

# Открытие страниц
driver.get("https://itcareerhub.de/ru/") # Открывается первая страница

driver.get("https://www.berlin.de") # Открывается вторая страница

driver.back() # Возвращаемся на itcareerhub.de/ru

driver.forward() # Переходим снова на berlin.de

# Задержка
sleep(5) # Скрипт "засыпает" на 5 секунд