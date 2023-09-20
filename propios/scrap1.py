from bs4 import BeautifulSoup

raw_html = """
<h1>Coche de segunda mano en venta</h1>
<ul class="cars-listing">
    <li class="car-listing">
        <div class="car-title">
            Volkswagen Escarabajo
        </div>
        <div class="car-description">
            <span class="car-make">Volkswagen</span>
            <span class="car-model">Escarabajo</span>
            <span class="car-build">1973</span>
        </div>
        <div class="sales-price">
            € <span class="car-price">14.998,—</span>
        </div>  
    </li>    
</ul>    
 """

# Analizar sintácticamente el texto fuente HTML guardado en raw_html
html = BeautifulSoup(raw_html, 'html.parser')
# Extraer el contenido de la etiqueta con la clase 'car-title'
car_title = html.find(class_='car-title').text.strip()
# Si el coche en cuestión resulta ser un Volkswagen Escarabajo
if (car_title == 'Volkswagen Escarabajo'):
    # Subir del título del coche a la siguiente etiqueta de elemento de lista <li></li>
    html.find_parent('li')

    # Determinar el precio del coche
    car_price = html.find(class_='sales-price').text.strip()

    # Mostrar el precio del coche
    print(car_price)


# Importar módulos
import requests
import csv
from bs4 import BeautifulSoup
# Dirección de la página web
url = "http://quotes.toscrape.com/"
# Ejecutar GET-Request
response = requests.get(url)
# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')
# Extraer todas las citas y autores del archivo HTML
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")
# Crear una lista de las citas
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)
# Crear una lista de los autores
authors = list()
for author in authors_html:
    authors.append(author.text)
# Para hacer el test: combinar y mostrar las entradas de ambas listas
for t in zip(quotes, authors):
    print(t)
# Guardar las citas y los autores en un archivo CSV en el directorio actual
# Abrir el archivo con Excel / LibreOffice, etc.
with open('./zitate.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))