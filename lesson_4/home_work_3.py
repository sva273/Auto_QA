import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()


def test_logos_displayed(driver):
    logos = driver.find_elements(By.CSS_SELECTOR, "a[href='/ru'] img")
    assert len(logos) >= 2, "Ожидалось минимум 2 логотипа"
    for logo in logos:
        assert logo.is_displayed(), "Один из логотипов не отображается"


@pytest.mark.parametrize("link_text", [
    "Программы",
    "Способы оплаты",
    "Новости",
    "О нас",
    "Отзывы"
])


def test_links_displayed(driver, link_text):
    link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, link_text))
    )
    assert link.is_displayed(), f"Ссылка '{link_text}' не отображается"



def test_language_buttons(driver):
    # RU кнопка
    lang_ru = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.t396__elem a[href='/ru']"))
    )

    # DE кнопка (текст 'de', href='/')
    lang_de = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'t396__elem')]//a[text()='de']"))
    )

    assert lang_ru.is_displayed(), "Кнопка RU не отображается"
    assert lang_de.is_displayed(), "Кнопка DE не отображается"


def test_contact_form_text(driver):

    popup_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#popup:form-tr3']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", popup_button)
    driver.execute_script("arguments[0].click();", popup_button)

    popup = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.t-popup_show"))
    )

    contact_text_elem = popup.find_element(By.XPATH, ".//div[string-length(text()) > 0]")

    contact_text = contact_text_elem.text.strip().splitlines()[0]

    expected_text = "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"
    assert contact_text == expected_text, (
        f"Ожидалось: '{expected_text}', найдено: '{contact_text}'"
    )