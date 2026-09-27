from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Login']")
    WARNING_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):

        self.enter_text(
            self.EMAIL,
            email
        )

    def enter_password(self, password):

        self.enter_text(
            self.PASSWORD,
            password
        )

    def click_login(self):

        self.click(
            self.LOGIN_BUTTON
        )

    def login(self, email, password):

        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_warning_message(self):

        return self.get_text(
            self.WARNING_MESSAGE
        )

    def wait_for_login_result(self, timeout=15):

        def condition(driver):
            title = driver.title
            if "My Account" in title:
                return True
            try:
                if self.get_warning_message():
                    return True
            except Exception:
                pass
            return False

        WebDriverWait(self.driver, timeout).until(condition)
        return "My Account" in self.driver.title