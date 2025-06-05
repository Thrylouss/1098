import pytest
from selenium import webdriver

@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://my.proweb.uz/log-in")
adfherhetheth

    yield driver

    driver.quit()