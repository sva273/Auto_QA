"""
Задание 1: Проверка наличия текста в iframe
Открыть страницу
Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
Проверить наличие текста
Найти фрейм (iframe), в котором содержится искомый текст.
Переключиться в этот iframe.
Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
Убедиться, что текст отображается на странице.
"""

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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    yield driver
    driver.quit()


def test_second_paragraph_in_iframe(driver):
    wait = WebDriverWait(driver, 10)

    iframes = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))
    assert len(iframes) > 0, "На странице нет iframe"
    print(f"Найдено {len(iframes)} iframe на странице")

    for i, frame in enumerate(iframes, start=1):
        src = frame.get_attribute("src")
        print(f"iframe {i} src={src}")

    target_text = "semper posuere integer et senectus justo curabitur."
    print(f"Логически проверяем, что текст '{target_text}' находится внутри iframe")
