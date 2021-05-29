from selenium.webdriver.common.by import By

from Python_Package import DriverClass


def findElement(locator):
    ele=DriverClass.driver.find_element(By.XPATH,locator)
    return ele


def getURL(URL):
    DriverClass.driver.get(URL)