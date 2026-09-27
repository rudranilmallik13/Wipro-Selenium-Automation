import os
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utilities.csv_reader import CSVReader
from utilities.config_reader import ConfigReader


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
VALID_LOGIN_EMAILS = {"rudranil.mallik2023@iem.edu.in"}


def row_is_valid_login(data):
    email = str(data.get("email", "")).strip()
    password = str(data.get("password", "")).strip()
    return email in VALID_LOGIN_EMAILS and password == "Test@123"


valid_rows = [data for data in test_data if row_is_valid_login(data)]


@pytest.mark.parametrize(
    "data",
    valid_rows
)
def test_product_search(driver, data):

    driver.get(BASE_URL)

    home = HomePage(driver)
    login = LoginPage(driver)

    home.click_my_account()
    home.click_login()

    login.login(
        data["email"].strip(),
        data["password"].strip()
    )

    assert login.wait_for_login_result(), "Login failed before product search."

    search = SearchPage(driver)
    home.search_product(
        data["product"]
    )

    assert search.is_product_displayed(
        data["product"]
    )