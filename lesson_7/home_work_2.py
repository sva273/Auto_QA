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
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    yield driver
    driver.quit()


def test_drag_and_drop(driver):
    wait = WebDriverWait(driver, 10)
    accept_button = wait.until(EC.visibility_of_element_located((By.XPATH, "(//p[@class='fc-button-label'])[1]")))
    accept_button.click()

    iframe = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame"))
    )
    driver.switch_to.frame(iframe)

    first_image = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li"))
    )[0]
    trash = wait.until(EC.presence_of_element_located((By.ID, "trash")))

    actions = ActionChains(driver)
    actions.click_and_hold(first_image).pause(0.5).move_to_element(trash).pause(0.5).release().perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    trash_items = driver.find_elements(By.CSS_SELECTOR, "#trash li")
    assert len(trash_items) == 1

    gallery_items = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
    assert len(gallery_items) == 3
