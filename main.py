import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from Funciones.Funcion import Funciones_Globales

t =2

def get_Data():
    return [
        ("//button[@class='Button'][contains(.,'5')]", "//button[@id='add']", "//button[@class='Button'][contains(.,'5')]", "10"),
        ("//button[@class='Button'][contains(.,'3')]", "//button[@class='Button'][contains(.,'-')]", "//button[@class='Button'][contains(.,'2')]", "1"),
        ("//button[@class='Button'][contains(.,'3')]", "//button[@id='add']", "//button[@class='Button'][contains(.,'2')]", "7"),
    ]

@pytest.mark.run
def test_caso0():
    global webdriver
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)
    f.Navegar("http://localhost/faefc3221188c0f1c520463a60c736e78708712fe86ade1d549694e0b8703772",t)
    f.Click_Mixto("Xpath","//button[@class='Button'][contains(.,'5')]",t)


@pytest.mark.run
@pytest.mark.parametrize("num1, act, num2, re",get_Data())
def test_caso1(num1, act, num2, re):
    global webdriver
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)
    f.Navegar("http://localhost/faefc3221188c0f1c520463a60c736e78708712fe86ade1d549694e0b8703772",t)
    f.Click_Mixto("Xpath", num1, t)
    f.Click_Mixto("Xpath", act, t)
    f.Click_Mixto("Xpath", num2, t)
    f.Click_Mixto("Xpath", "//button[@class='Button'][contains(.,'=')]", t)
    result = f.SEX("//input[@class='DisplayText']").get_attribute("value")
    assert result == re

