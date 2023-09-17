import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


s = Service("C:/Users/romer.D-PC/PycharmProjects/ProgramacionFuncional/5toSemestre/meta1_3/webdriver/chromedriver.exe")
opc = Options()
opc.add_argument("--windows-size = 1000, 1200")


navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("https://www.amazon.com.mx/")

txtSearch = navegador.find_element(By.NAME, "field-keywords")
txtSearch.send_keys("Sudaderas Nike")

btnSearch = navegador.find_element(By.ID, "nav-search-submit-button")
btnSearch.click()

navegador.save_screenshot("Amazon_Screenshot.png")
time.sleep(2)