from NewPack import DriverClass
from selenium.webdriver.common.by import By
#The function to get URL
def getUrl(url):
    DriverClass.driver.get(url)

#Any Fucntion where locator is X path
def getElement(locator):
    ele=DriverClass.driver.find_element(By.XPATH,locator)
    return  ele
