# David Romero Ramos 952
"""
Realizar una función que reciba como parámetro un DataFrame y un máximo porcentaje.
Este debe eliminar todas las columnas que superen o igualen el máximo porcentaje de valores nulos establecidos en el
DataFrame Original. Retornar la lista nombres de columnas eliminadas.  Validar que el porcentaje máximo esté entre 0 y 1."""

import pandas as pd

def eliminar_columnas_nulas(df, porcentaje):
    if not 0 <= porcentaje <= 1:
        raise ValueError("El porcentaje máximo debe estar entre 0 y 1")
    max_nulos_por_columna = porcentaje * len(df)
    columnas_a_eliminar = df.columns[df.isnull().sum() >= max_nulos_por_columna].tolist()
    return columnas_a_eliminar


data = {
    'A': [None, None, None, 4],
    'B': [5, None, 7, 8],
    'C': [9, 10, 11, 12],
    'D': [None, None, 15, 16]
}

df = pd.DataFrame(data)

columnas_eliminadas = eliminar_columnas_nulas(df, 0.50)
print(f"\nColumnas eliminadas: {columnas_eliminadas}")
df_nuevo = df.drop(columns=columnas_eliminadas)
print(df_nuevo)