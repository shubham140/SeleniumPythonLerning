import pytest
from selenium import  webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_runGoogle():
    gf=webdriver.Chrome(ChromeDriverManager().install())
    gf.get("http://google.com")
    wait=WebDriverWait(gf,10)
    wait.until(expected_conditions.title_is("Google"))
    assert gf.title=="Google","On no fail"
    gf.quit()

def test_runYouTube():
    gf = webdriver.Chrome(ChromeDriverManager().install())
    gf.get("https://www.youtube.com/")
    wait=WebDriverWait(gf,30)
    wait.until(expected_conditions.title_is("Youtube"))
    assert gf.title=="YouTube","On no fail"
    gf.quit()
def test_runPrimeVideo():
    gf = webdriver.Chrome(ChromeDriverManager().install())
    wait=WebDriverWait(gf,30)
    gf.get("https://www.primevideo.com/storefront/home/ref=atv_nb_logo")
    wait.until(expected_conditions.title_is("Prime Video"))
    assert gf.title=="Prime Video","On no fail"
    gf.quit()
