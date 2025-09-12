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

    try:
        consent_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[@class='fc-button-label' and text()='Соглашаюсь']"))
        )
        consent_btn.click()
        wait.until(EC.invisibility_of_element(consent_btn))
    except:
        pass

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
    assert len(trash_items) == 1, f"Ожидалось 1 фото в корзине, найдено {len(trash_items)}"

    gallery_items = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
    assert len(gallery_items) == 3, f"Ожидалось 3 фото в галерее, найдено {len(gallery_items)}"