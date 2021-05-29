from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver1=webdriver.chrome(ChromeDriverManager().install())

driver1.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

time.sleep(15)

driver1.find_element(By.XPATH,"//input[@id='justAnInputBox']");
time.sleep(5)
lst=driver1.find_elements(By.XPATH,"//*[@id='comboTree905339DropDownContainer']");
for i in range(len(lst)):
    print(lst[i].text)
