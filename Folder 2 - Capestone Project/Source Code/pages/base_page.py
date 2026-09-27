from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.config_reader import ConfigReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        config = ConfigReader()

        self.wait_time = int(
            config.get("explicit_wait")
        )

        self.wait = WebDriverWait(
            driver,
            self.wait_time
        )

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    def enter_text(self, locator, text):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(text)

    def get_text(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    def is_displayed(self, locator):

        try:

            self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return True

        except Exception:

            return False