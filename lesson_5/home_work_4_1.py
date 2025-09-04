import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()


def test_loading_images(driver):
    fourth_img_locator = (By.XPATH, "(//img)[4]")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(fourth_img_locator)
    )
    WebDriverWait(driver, 20).until(
        EC.element_attribute_to_include(fourth_img_locator, "src")
    )

    images = driver.find_elements(By.TAG_NAME, "img")
    assert len(images) == 4, f"Ожидалось 4 изображения, найдено {len(images)}"

    award_img = next((img for img in images if img.get_attribute("alt") == "award"), None)
    assert award_img is not None, "Изображение с alt='award' не найдено"
    assert award_img.get_attribute("alt") == "award"