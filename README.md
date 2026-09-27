# TutorialsNinja E-Commerce Automation Framework

## 📌 Project Overview

This project is a Selenium-based Web Automation Framework developed using **Python, Selenium WebDriver, PyTest, Page Object Model (POM), CSV Test Data, Configuration Management, Screenshots, and HTML Reporting**.

The framework automates the login and product search functionalities of the **TutorialsNinja Demo E-Commerce application**.

The main objective is to demonstrate how a scalable and maintainable Selenium automation framework can be designed using industry-standard automation practices.

---

## 🌐 Application Under Test

**Application:** TutorialsNinja Demo E-Commerce Website

**URL:** https://tutorialsninja.com/demo/

The application provides common e-commerce functionalities such as:

- User Login
- Product Search
- Product Categories
- Product Details
- Shopping Cart
- Account Management

---

# 🎯 Project Objectives

The main objectives of this project are:

- Automate web application functionality using Selenium WebDriver.
- Implement the Page Object Model (POM).
- Use PyTest for test execution.
- Demonstrate Unittest integration.
- Implement reusable utility classes.
- Read test data from CSV files.
- Manage configuration using `config.ini`.
- Implement explicit waits for stable test execution.
- Capture screenshots automatically when tests fail.
- Generate HTML execution reports.
- Create a maintainable and scalable automation framework.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Selenium WebDriver | Web Browser Automation |
| PyTest | Test Execution Framework |
| Unittest | Unit Testing Demonstration |
| Page Object Model | Framework Design Pattern |
| Chrome WebDriver | Browser Automation |
| CSV | Test Data Management |
| ConfigParser | Configuration Management |
| PyTest HTML | HTML Test Reporting |

---

# 📂 Project Structure

```text
TutorialsNinja_Automation/
│
├── config/
│   └── config.ini
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   └── search_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_search.py
│   └── test_unittest.py
│
├── utilities/
│   ├── config_reader.py
│   ├── csv_reader.py
│   └── screenshot.py
│
├── test_data/
│   └── testdata.csv
│
├── screenshots/
│   └── failure_screenshots.png
│
├── reports/
│   └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
