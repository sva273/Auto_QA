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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()

def test_validation_form(driver):
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Hans")
    #LAst NAme
    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Schmidt")
    #Address
    address = driver.find_element(By.NAME, "address")
    address.send_keys("Hauptstrasse 5")
    #City
    city = driver.find_element(By.NAME, "city")
    city.send_keys("Berlin")
    #Country
    country = driver.find_element(By.NAME, "country")
    country.send_keys("Germany")
    #Email
    email = driver.find_element(By.NAME, "e-mail")
    email.send_keys("afsgdfasd@gmail.com")
    #Phone number
    phone = driver.find_element(By.NAME, "phone")
    phone.send_keys("+49123456789")
    #Job position
    job_position = driver.find_element(By.NAME, "job-position")
    job_position.send_keys("QA Engineer")
    #company
    company = driver.find_element(By.NAME, "company")
    company.send_keys("Some Company")

    submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()


    first_name_result = driver.find_element(By.ID, "first-name")
    assert "alert-success" in first_name_result.get_attribute("class")

    last_name_result = driver.find_element(By.ID, "last-name")
    assert "alert-success" in last_name_result.get_attribute("class")

    address_result = driver.find_element(By.ID, "address")
    assert "alert-success" in address_result.get_attribute("class")

    city_result = driver.find_element(By.ID, "city")
    assert "alert-success" in city_result.get_attribute("class")

    country_result = driver.find_element(By.ID, "country")
    assert "alert-success" in country_result.get_attribute("class")

    email_result = driver.find_element(By.ID, "e-mail")
    assert "alert-success" in email_result.get_attribute("class")

    phone_result = driver.find_element(By.ID, "phone")
    assert "alert-success" in phone_result.get_attribute("class")

    job_position_result = driver.find_element(By.ID, "job-position")
    assert "alert-success" in job_position_result.get_attribute("class")

    company_result = driver.find_element(By.ID, "company")
    assert "alert-success" in company_result.get_attribute("class")

    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class")