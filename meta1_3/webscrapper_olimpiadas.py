
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

#s = Service(ChromeDriverManager().install())
s = Service("C:/Users/romer.D-PC/PycharmProjects/ProgramacionFuncional/5toSemestre/meta1_3/webdriver/chromedriver.exe")
opc = Options()
opc.add_argument("--windows-size = 1000, 1200")
#opc.add_argument("--headless=new")

navegador = webdriver.Chrome(service=s, options=opc)
navegador.get("http://www.olympedia.org/statistics/medal/country")

cmbYear = navegador.find_element(By.NAME, "edition_id")
cmbGender = navegador.find_element(By.NAME, "athlete_gender")

lista_gender = cmbGender.find_elements(By.TAG_NAME, "option")
lista_year = cmbYear.find_elements(By.TAG_NAME, "option")

print([item.text for item in lista_gender])
print([item.text for item in lista_year])

save_data = {"gender" : [],
             "year" : [],
             "country" : [],
             "gold" : [],
             "silver" : [],
             "bronze" : [],
             "total" : []}

for gender in lista_gender[1:]:
    gender.click()
    for year in lista_year[1:30]:
        year.click()
        soup = BeautifulSoup(navegador.page_source, "html.parser")
        tabla = soup.find("table")
        lista_paises = tabla.find_all("tr")
        for pais in lista_paises[1:]:
            save_data["gender"].append(gender.text)
            save_data["year"].append(year.text)
            valores = pais.find_all("td")
            save_data["country"].append(valores[0].text)
            save_data["gold"].append(valores[2].text)
            save_data["silver"].append(valores[3].text)
            save_data["bronze"].append(valores[4].text)
            save_data["total"].append(valores[5].text)


resultados = pd.DataFrame(save_data)
resultados.to_csv("olimpiadas1.csv")

time.sleep(2)