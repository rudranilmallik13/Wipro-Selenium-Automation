import csv
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.screenshot import capture_screenshot

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "test_data", "testdata.csv")

with open(CSV_PATH, mode="r", newline="", encoding="utf-8") as file:
    test_data = list(csv.DictReader(file))

config = ConfigReader()
BASE_URL = config.get("base_url")


@pytest.fixture
def driver():

    browser = config.get("browser")
    implicit_wait = int(config.get("implicit_wait"))

    if browser.lower() == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(implicit_wait)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):

    data = test_data[0]

    driver.get(BASE_URL)

    home = HomePage(driver)
    login = LoginPage(driver)

    home.click_my_account()
    home.click_login()

    login.login(
        data["email"].strip(),
        data["password"].strip()
    )

    if not login.wait_for_login_result():
        pytest.skip("Login failed; product search tests require a valid session.")

    return driver


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get("driver")
        if driver is not None:
            screenshot_name = item.name
            screenshot_path = capture_screenshot(driver, screenshot_name)
            print(f"\n[FAILURE SCREENSHOT] {screenshot_path}\n")