from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver=webdriver.Chrome(executable_path="C:\\Users\\Shubham\\OneDrive\\Desktop\\Study\\Selenium\\Broswer_Files\\chromedriver.exe")


driver.get("http://google.com")

sleep(20)

driver.find_element(By.NAME,"q").send_keys("Elon Musk")
sleep(10)
ele=driver.find_elements(By.XPATH,"//*[@class='erkvQe']/li/div/div[@class='pcTkSc']/div/span")

for i in ele:
    print(i.text)
    if(i=="elon musk bitcoin"):
        i.click()


