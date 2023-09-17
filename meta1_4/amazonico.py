import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scrape_amazon_product_info(search_query, num_pages):
    s = Service("C:/Users/romer.D-PC/PycharmProjects/ProgramacionFuncional/5toSemestre/meta1_3/webdriver/chromedriver.exe")
    opc = Options()
    opc.add_argument("--window-size=1000,1200")

    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.amazon.com.mx/")

    txtSearch = navegador.find_element(By.NAME, "field-keywords")
    txtSearch.send_keys(search_query)
    txtSearch.send_keys(Keys.RETURN)

    time.sleep(2)

    save_data = {
        "Nombre del Producto": [],
        "Rating": [],
        "Precio": [],
        "Fecha de Entrega": []
    }

    for page in range(num_pages):
        page_source = navegador.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        products = soup.find_all("div", class_="s-result-item")

        for product in products:
            product_name_elem = product.find("span", class_="a-text-normal")
            product_rating_elem = product.find("span", class_="a-icon-alt")
            product_price_elem = product.find("span", class_="a-offscreen")
            product_delivery_elem = product.find("span", class_="a-text-bold")

            product_name = product_name_elem.text if product_name_elem else "No disponible"
            product_rating = product_rating_elem.text if product_rating_elem else "No disponible"
            product_price = product_price_elem.text if product_price_elem else "No disponible"
            product_delivery_date = product_delivery_elem.text if product_delivery_elem else "No disponible"

            save_data["Nombre del Producto"].append(product_name)
            save_data["Rating"].append(product_rating)
            save_data["Precio"].append(product_price)
            save_data["Fecha de Entrega"].append(product_delivery_date)

        try:
            next_page_button = navegador.find_element(By.PARTIAL_LINK_TEXT, "Siguiente")
            next_page_button.click()
            time.sleep(2)
        except:
            break

    navegador.quit()

    df = pd.DataFrame(save_data)
    df.to_csv("amazon_product_info.csv", index=False)

if __name__ == "__main__":
    busqueda = "Nike"
    paginas = 5
    scrape_amazon_product_info(busqueda, paginas)
