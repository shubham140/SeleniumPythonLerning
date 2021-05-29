import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(params=["chrome","firefox"],scope="class")
def ini_driver(request):
    if(request.param=="chrome"):
        web_driver=webdriver.Chrome(ChromeDriverManager().install())
        request.cls.driver=web_driver
    if(request.param=="firefox"):
        web_driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("ini_driver")
class Test_Google():
    pass

class Test_Google(Test_Google):

    def test_google(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title=="Google"



