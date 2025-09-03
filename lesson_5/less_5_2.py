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
    driver.get("http://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()


def test_success_auth(driver):
    wait = WebDriverWait(driver, 1)
    username_input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='username']")))
    username_input_field.send_keys("Admin")

    password_input_field = driver.find_element(By.NAME, "password")
    password_input_field.send_keys("admin123")

    login_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button.click()
    header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h6")))
    assert header.text == "Dashboard"