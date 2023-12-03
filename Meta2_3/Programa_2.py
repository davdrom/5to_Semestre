# David Romero Ramos 952
"""
Realizar una función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados.
"""
import pandas as pd

def contar_duplicados(dataframe):
    duplicados = dataframe.duplicated().sum()
    return duplicados

d = {
    "1": [1, 2, 2],
    "2": [1, 2, 2],
    "3": [10, 20, 20]
}

df = pd.DataFrame(d)

n = contar_duplicados(df)
print("Filas duplicadas:", n)
