from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
opt=webdriver.ChromeOptions()
#opt.headless=True
opt.add_argument("--incognito")
driver=webdriver.Chrome(ChromeDriverManager().install(),options=opt)






