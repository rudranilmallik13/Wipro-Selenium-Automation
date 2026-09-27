import os

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utilities.csv_reader import CSVReader
from utilities.config_reader import ConfigReader
from utilities.screenshot import capture_screenshot


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

CSV_PATH = os.path.join(
    BASE_DIR,
    "test_data",
    "testdata.csv"
)

test_data = CSVReader.read_data(
    CSV_PATH
)

config = ConfigReader()

BASE_URL = config.get("base_url")


def test_login_and_search_per_row(driver):

    valid_search_count = 0

    for index, data in enumerate(test_data, start=1):
        try:
            driver.get(BASE_URL)

            home = HomePage(driver)
            login = LoginPage(driver)

            home.click_my_account()
            home.click_login()

            login.login(
                data["email"].strip(),
                data["password"].strip()
            )

            login_success = login.wait_for_login_result()

            if not login_success:
                screenshot_name = f"login_failed_row_{index}_{data['email']}"
                screenshot_path = capture_screenshot(driver, screenshot_name)
                print(f"Row {index} login failed: {data['email']} -> screenshot: {screenshot_path}")
                continue

            home.search_product(data["product"])
            search = SearchPage(driver)
            assert search.is_product_displayed(data["product"]), (
                f"Product search failed for row {index}: {data['product']}"
            )

            valid_search_count += 1
            print(f"Row {index} passed: {data['email']} -> {data['product']}")

        except AssertionError:
            screenshot_name = f"row_{index}_assertion_failed"
            screenshot_path = capture_screenshot(driver, screenshot_name)
            print(f"Assertion failed for row {index}: screenshot: {screenshot_path}")
            raise

        except Exception as exc:
            screenshot_name = f"row_{index}_exception"
            screenshot_path = capture_screenshot(driver, screenshot_name)
            print(f"Exception in row {index}: {exc} -> screenshot: {screenshot_path}")
            raise

    assert valid_search_count >= 1, "No valid login rows completed product search."