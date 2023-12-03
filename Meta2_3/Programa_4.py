# David Romero Ramos 952
"""
Realizar una función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar y una cadena.
La cadena solo puede ser mean, bfill o ffill, en caso contrario lanzar una excepción.
Debe sustituir los valores nulos por el método especificado y retornar el DataFrame modificado.
"""

import pandas as pd

def llenar_nulos_por_metodo(df, columnas, metodo):
    if metodo not in ['mean', 'bfill', 'ffill']:
        raise ValueError("El método debe ser 'mean', 'bfill' o 'ffill'")

    columnas_validas = set(columnas)
    columnas_no_validas = columnas_validas - set(df.columns)
    if columnas_no_validas:
        raise ValueError(f"Las columnas {columnas_no_validas} no existen en el DataFrame")

    for columna in columnas:
        if metodo == 'mean':
            df[columna].fillna(df[columna].mean(), inplace=True)
        elif metodo == 'bfill':
            df[columna].bfill(inplace=True)
        elif metodo == 'ffill':
            df[columna].ffill(inplace=True)

    return df

data = {
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': [9, 10, 11, None],
    'D': [13, None, 15, 16]
}

df = pd.DataFrame(data)
print(df)
df_nuevo = llenar_nulos_por_metodo(df, ['A', 'B'], 'mean')
print(df_nuevo)