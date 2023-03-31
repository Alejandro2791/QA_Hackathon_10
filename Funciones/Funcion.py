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

class Funciones_Globales():

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Pagina abierta "+Url)
        t = time.sleep(Tiempo)
        return t

    def SEX(self, elemento):
        val = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, elemento)))
        #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, elemento)))
        #val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def Texto_Mixto(self, tipo, selector, texto, Tiempo):
        try:
            if(tipo == "Xpath"):
                val = self.SEX(selector)
            elif (tipo == "ID"):
                val = self.SEI(selector)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo {} el texto {}".format(selector, texto))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento {}".format(selector,))

    def Texto_Mixto1(self, tipo, selector, texto, Tiempo):
        try:
            if (tipo == "Xpath"):
                val = self.SEX(selector)
            elif (tipo == "ID"):
                val = self.SEI(selector)
            val.clear()
            val.send_keys(texto + Keys.TAB)
            print("Escribiendo en el campo {} el texto {}".format(selector, texto))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento {}".format(selector, ))

    def Click_Mixto(self, tipo, selector, Tiempo):
        try:
            if(tipo == "Xpath"):
                val = self.SEX(selector)
            elif (tipo == "ID"):
                val = self.SEI(selector)
            val.click()
            print("Dando click en el elemento {}".format(selector))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento {}".format(selector,))

    def Select_Mixto(self, tipoSelec, tipo, selector, dato, Tiempo):
        try:
            if (tipoSelec == "Xpath"):
                val = self.SEX(selector)
            elif (tipoSelec == "ID"):
                val = self.SEI(selector)
            val = Select(val)
            if (tipo == "Texto"):
                val.select_by_index(dato)
            elif (tipo == "Index"):
                val.select_by_index(dato)
            elif (tipo == "Value"):
                val.select_by_value(dato)
            print("El campo seleccionado es {}".format(dato))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento {}".format(selector))

    def Upload_Xpath(self, xpath, ruta, Tiempo):
        try:
            val = self.SEX(xpath)
            val.send_keys(ruta)
            print("Se carga el archivo {}".format(ruta))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento {}".format(xpath))