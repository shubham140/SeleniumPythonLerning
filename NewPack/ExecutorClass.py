from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from NewPack import DriverClass
from NewPack import  General_Functions
import time

General_Functions.getUrl("https://opensource-demo.orangehrmlive.com/")

username="//*[@id='txtUsername']"
password="//*[@id='txtPassword']"
loginBttn="//input[@type='submit']"
wait=WebDriverWait(DriverClass.driver,20)
wait.until(ec.visibility_of_element_located((By.XPATH,username)))
General_Functions.getElement(username).send_keys("Admin")
General_Functions.getElement(password).send_keys("admin123")
General_Functions.getElement(loginBttn).click()
DriverClass.driver.implicitly_wait(10)
Admin_Btn="//b[contains(text(),'Admin')]"
management_Btn="//*[contains(text(),'User Management')]"
users="//*[contains(text(),'Users')]"
ele1=General_Functions.getElement(Admin_Btn)
ele2=General_Functions.getElement(management_Btn)
ele3=General_Functions.getElement(users)
action=ActionChains(DriverClass.driver)
action.move_to_element(ele1).perform()
action.move_to_element(ele2).perform()
action.click(ele3).perform()
table="//*[@id='resultTable']"
table_ele=DriverClass.driver.find_elements(By.XPATH,table)

table_name="//*[@id='resultTable']/tbody/tr/td[2]/a"
table_ele_name=DriverClass.driver.find_elements(By.XPATH,table_name)

for i in table_ele_name:

    if(i.text=="Goutam.Ganesh"):
        print(i.text)
        i.click()
        break

DriverClass.driver.back()
DriverClass.driver.get_screenshot_as_file("MyScreeshot.png")
