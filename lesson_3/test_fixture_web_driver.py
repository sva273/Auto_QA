from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    # Инициализация WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Максимизация окна
    driver.maximize_window()
    # Передача драйвера в тест
    yield driver
    # Закрытие браузера
    driver.quit()


def test_open_about_page(driver):
    # Открытие сайта
    driver.get("https://itcareerhub.de/ru")

    about_link = driver.find_element(By.LINK_TEXT, "О нас")
    about_link.click()
    sleep(3)