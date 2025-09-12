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
    driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
    yield driver
    driver.quit()



def test_drag_and_drop(driver):
    draggable = driver.find_element(By.ID, "draggable")
    droppable = driver.find_element(By.ID, "droppable")
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable).perform()
    ##CHeck that text "Dropped!" is displayed
    assert droppable.text == "Dropped!"


