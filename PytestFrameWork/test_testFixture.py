import pytest
import pytest
from selenium import  webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def init_driver():
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)

    yield
    driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_testTile():
    assert driver.title=="Google"