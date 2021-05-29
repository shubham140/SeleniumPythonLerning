from selenium import webdriver   #impoted selenium webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(executable_path="C:\\Users\\Shubham\\OneDrive\\Desktop\\Study\\Selenium\\Broswer_Files\\chromedriver.exe")

driver.get("https://www.freecrm.com/index.html")
print(driver.title)
delay = 10 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Log In')]")))
   # print "Page is ready!"
except TimeoutException:
    print("Oh noo!!!!")
driver.find_element(By.XPATH,"//*[contains(text(),'Log In')]").click()






