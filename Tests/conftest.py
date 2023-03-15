import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        service_obj = Service("C:\\Users\\Lenovo\\Downloads\\geckodriver-v0.32.2-win64\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "chrome":
        service_obj = Service("C:\\Users\\Lenovo\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
