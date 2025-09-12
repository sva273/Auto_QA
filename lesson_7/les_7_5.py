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
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://crossbrowsertesting.github.io/hover-menu.html")
    yield driver
    driver.quit()


def test_hover(driver):
    dropdown = driver.find_element(By.XPATH, "(//a[@class = 'dropdown-toggle'])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(dropdown).perform()
    secondary_menu = driver.find_element(By.LINK_TEXT, "Secondary Menu")
    actions.move_to_element(secondary_menu).perform()
    secondary_action = driver.find_element(By.LINK_TEXT, "Secondary Action")
    secondary_action.click()
    header = driver.find_element(By.XPATH, "(//h1)[2]")
    assert header.text == "Secondary Page"