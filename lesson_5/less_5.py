from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://example.com")

wait = WebDriverWait(driver, 10) # Ожидание до 10 секунд
element = wait.until(EC.presence_of_element_located((By.ID, "some_id"))) # Ждём, пока элемент появится в DOM

# Или ждём, пока элемент станет кликабельным:
clickable_element = wait.until(EC.element_to_be_clickable((By.ID, "button_id")))
clickable_element.click()

