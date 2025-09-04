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
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()


def test_text_input(driver):
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("ITCH")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    assert button.text == "ITCH", f"Ожидалось: 'ITCH', а найдено: '{button.text}'"
