import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



@pytest.fixture
def driver():
    # Инициализация WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Максимизация окна
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://suninjuly.github.io/cats.html")
    # Передача драйвера в тест
    yield driver
    # Закрытие браузера
    driver.quit()



#Check that name of the second cat card is "Serious Cat"
def test_name_of_second_cat(driver):
    page_header = driver.find_element(By.CSS_SELECTOR, "[class='jumbotron-heading-55']")
    assert page_header.text == "Serious cat"


def test_name_of_second_cat2(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    second_cat = driver.find_element(By.XPATH, "//p[contains(@class, 'second')]")
    assert second_cat.text == "Serious cat"



def test_9mins_text(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    second_9min = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(5) small")
    assert second_9min.text == "9 mins"


def test_9mins_text_2(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    second_9min = driver.find_element(By.XPATH, '(//div[@class="col-sm-4"])[5]//small')
    assert second_9min.text == "9 mins"


def test_cats_album_text_2(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    album_title = driver.find_element(By.XPATH, "//strong[text()='Cats album']")
    assert album_title.text == "Cats album"

