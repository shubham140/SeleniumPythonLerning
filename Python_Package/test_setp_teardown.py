import pytest
import pytest
from selenium import  webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def setup_module(module):
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)

def teardown_module(module):
    driver.quit()


def test_testTile():
    assert driver.title=="Google"

