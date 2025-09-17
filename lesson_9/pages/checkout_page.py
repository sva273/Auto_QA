from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-header")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT)).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def continue_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def finish_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

    def get_complete_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_TEXT)).text

    def get_total_price(self):
        total_element = self.wait.until(EC.visibility_of_element_located(self.TOTAL_LABEL))
        return total_element.text.split(": ")[1]  # возвращает "$58.29"
