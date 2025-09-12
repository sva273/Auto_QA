from time import sleep
import math
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
    driver.get("https://suninjuly.github.io/math.html")
    yield driver
    driver.quit()


def math_calc(x):
      return math.log(abs(12 * math.sin(x)))


def test_math_calc(driver):
    x_value = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input_value"))).text
    result = math_calc(int(x_value))
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(str(result))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "robotCheckbox"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "robotsRule"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))).click()
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_text = alert.text
    assert "Congrats, you've passed the task!" in alert_text
    alert.accept()



def test_math_calc1(driver):
    x_value = driver.find_element(By.ID, "input_value").text
    result = math_calc(int(x_value))
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(str(result))
    check_box = driver.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    check_box.click()
    radio_box = driver.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radio_box.click()
    submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()
    wait = WebDriverWait(driver,20)
    alert = wait.until(EC.alert_is_present())
    assert "Congrats, you've passed the task!" in alert.text