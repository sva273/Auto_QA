from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc_45(driver):
    delay_input_field = driver.find_element(By.ID, "delay")
    delay_input_field.clear()
    delay_input_field.send_keys("45")
    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()
    button_plus = driver.find_element(By.XPATH,"//span[text()='+']")
    button_plus.click()
    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()
    button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"

