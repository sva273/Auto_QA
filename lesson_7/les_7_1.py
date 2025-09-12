from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from typing_extensions import assert_type
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://suninjuly.github.io/huge_form.html")
    yield driver
    driver.quit()


def test_alert_text(driver):
    input_fields = driver.find_elements(By.CSS_SELECTOR, "[type='text']")
    for field in input_fields:
        field.send_keys("Hello")
    submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())
    assert "Congrats, you've passed the task!" in alert.text