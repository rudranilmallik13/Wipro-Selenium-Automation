from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):

    PRODUCT_NAMES = (
        By.CSS_SELECTOR,
        ".product-thumb h4 a"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_names(self):

        elements = self.wait.until(
            lambda driver: driver.find_elements(
                *self.PRODUCT_NAMES
            )
        )

        return [
            element.text
            for element in elements
        ]

    def is_product_displayed(
        self,
        expected_product
    ):

        products = self.get_product_names()

        return any(
            expected_product.lower()
            in product.lower()
            for product in products
        )