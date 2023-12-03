# David Romero Ramos 952
"""
Realizar una función que reciba como parámetro un DataFrame y  retorne el porcentaje de valores nulos de cada columna.
"""
import pandas as pd

def porcentaje_nulos(dataframe):
    porcentaje_nulos = (dataframe.isnull().mean()) * 100

    return porcentaje_nulos


d = {
    '1': [1, 2, 3, 4, 5],
    '2': [None, 2, 3, None, 5],
    '3': [None, None, None, None, None]
}

df = pd.DataFrame(d)

r = porcentaje_nulos(df)
print(r)



