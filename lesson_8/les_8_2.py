import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/file_input.html")
    yield driver
    driver.quit()

def test_upload_file_form(driver):
    first_name = driver.find_element(By.NAME, "firstname")
    first_name.send_keys("Hans")

    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys("Schmidt")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("afsgdfasd@gmail.com")

    file_path = os.path.abspath("test_file.txt")
    with open(file_path, "w") as f:
        f.write("Hello, this is a test file.")

    file_input = driver.find_element(By.NAME, "file")
    file_input.send_keys(file_path)

    submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()
    wait = WebDriverWait(driver, 20)
    alert = wait.until(EC.alert_is_present())
    assert "Congrats, you've passed the task!" in alert.text