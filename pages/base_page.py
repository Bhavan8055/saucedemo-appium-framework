from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.logger = get_logger("BasePageLogger")

    def wait_for_element(self, locator_type, locator_value):
        self.logger.info(f"Waiting for element: {locator_value}")
        return self.wait.until(
            EC.presence_of_element_located((locator_type, locator_value))
        )

    def click_element(self, locator_type, locator_value):

        element = self.wait.until(
        EC.element_to_be_clickable((locator_type, locator_value))
    )

        element.click()

        self.logger.info(f"Clicked element: {locator_value}")

    def input_text(self, locator_type, locator_value, text):
        element = self.wait_for_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator_type, locator_value):
        element = self.wait_for_element(locator_type, locator_value)
        return element.text

    def is_element_displayed(self, locator_type, locator_value):
        try:
            return self.wait_for_element(
                locator_type,
                locator_value
            ).is_displayed()
        except:
            return False