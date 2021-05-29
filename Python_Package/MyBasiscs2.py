from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import *
import WebDriverManager
from selenium.webdriver.common.by import By



WebDriverManager.driver.maximize_window()
WebDriverManager.driver.get("https://pypi.org/project/webdriver-manager/")
WebDriverManager.driver.find_element(By.XPATH,"").send_keys(Keys.Enter)