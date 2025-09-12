import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    yield driver
    driver.quit()

def math_calc(x):
    return math.log(abs(12 * math.sin(x)))

def test_switch_tab(driver):
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    tabs_ids = driver.window_handles
    driver.switch_to.window(tabs_ids[1])

    wait = WebDriverWait(driver, 10)
    x_element = wait.until(EC.presence_of_element_located((By.ID, "input_value")))
    x_value = x_element.text
    print(f"x_value: {x_value}")

    result = math_calc(int(x_value))
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(str(result))
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Alert text: {alert_text}")

    assert "Congrats, you've passed the task!" in alert_text

    alert.accept()


def test_switch_alert(driver):
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    tabs_ids = driver.window_handles
    print(tabs_ids)
    driver.switch_to.window(tabs_ids[1])

    x_value = driver.find_element(By.ID, "input_value").text
    result = math_calc(int(x_value))
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(str(result))
    submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())
    assert "Congrats, you've passed the task!" in alert.text