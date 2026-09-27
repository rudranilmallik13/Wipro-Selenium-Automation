from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    MY_ACCOUNT = (
        By.XPATH,
        "//span[text()='My Account']"
    )

    LOGIN_LINK = (
        By.LINK_TEXT,
        "Login"
    )

    SEARCH_BOX = (
        By.NAME,
        "search"
    )

    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "button.btn.btn-default.btn-lg"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def click_my_account(self):

        self.click(
            self.MY_ACCOUNT
        )

    def click_login(self):

        self.click(
            self.LOGIN_LINK
        )

    def search_product(self, product):

        self.enter_text(
            self.SEARCH_BOX,
            product
        )

        self.click(
            self.SEARCH_BUTTON
        )