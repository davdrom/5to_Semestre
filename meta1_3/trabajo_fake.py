import pandas as pd
import requests
import pandas
from bs4 import BeautifulSoup

response = requests.get("https://realpython.github.io/fake-jobs/")
# print(response.status_code)
# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.body.section)
# soup.find()
lista_divs = soup.find_all("div", attrs={"class": "card-content"})


data = {"company": [],
        "name": [],
        "city": [],
        "date": []}


for div in lista_divs:
    titulo = div.find("h2", attrs={"class": "title is-5"})
    company = div.find("h3", attrs={"class": "subtitle is-6 company"})
    city = div.find("p", attrs={"class":"location"})
    date = div.find("time")

    data["company"].append(company.text)
    data["name"].append(titulo.text)
    data["city"].append(city.text.strip())
    data["date"].append(date.text)

# print(data)
data_df = pd.DataFrame(data)
print(data_df)
data_df.to_csv("trabajos.csv")

