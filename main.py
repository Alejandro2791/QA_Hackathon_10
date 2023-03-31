import time
import pytest
import allure
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
from allure_commons.types import AttachmentType

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
    allure.attach(driver.get_screenshot_as_png(), name="abrir_pagina", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("Xpath", num1, t)
    allure.attach(driver.get_screenshot_as_png(), name="capturar_num1", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("Xpath", act, t)
    allure.attach(driver.get_screenshot_as_png(), name="capturar_op", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("Xpath", num2, t)
    allure.attach(driver.get_screenshot_as_png(), name="capturar_num2", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("Xpath", "//button[@class='Button'][contains(.,'=')]", t)
    allure.attach(driver.get_screenshot_as_png(), name="resultado", attachment_type=AttachmentType.PNG)
    result = f.SEX("//input[@class='DisplayText']").get_attribute("value")
    assert result == re

@pytest.mark.run
@pytest.mark.parametrize("num1, act, num2, re",get_Data())
def test_caso5(num1, act, num2, re):
    global webdriver
    ser = Service("C:\Drivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Funciones_Globales(driver)
    f.Navegar("http://localhost/faefc3221188c0f1c520463a60c736e78708712fe86ade1d549694e0b8703772",t)
    allure.attach(driver.get_screenshot_as_png(), name="abrir_navegador1", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("Xpath", num1, t)
    allure.attach(driver.get_screenshot_as_png(), name="capturar_num3", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("Xpath", act, t)
    allure.attach(driver.get_screenshot_as_png(), name="capturar_op1", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("Xpath", "//button[@class='Button'][contains(.,'=')]", t)
    allure.attach(driver.get_screenshot_as_png(), name="resultado", attachment_type=AttachmentType.PNG)
    result = f.SEX("//input[@class='DisplayText']").get_attribute("value")
    assert result == re

