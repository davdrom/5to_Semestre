#Romero Ramos David 952

import pandas as pd

"""
Normaliza los datos de las columnas especificadas utilizando la técnica Min-Max usando solo pandas.
"""
def normalizar_min_max(df, columnas):


    columnas_validas = set(columnas)
    columnas_no_validas = columnas_validas - set(df.columns)
    if columnas_no_validas:
        raise ValueError(f"Las columnas {columnas_no_validas} no existen en el DataFrame")

    df_normalizado = df.copy()

    for columna in columnas:
        df_normalizado[columna] = (df_normalizado[columna] - df_normalizado[columna].min()) / \
                                  (df_normalizado[columna].max() - df_normalizado[columna].min())

    return df_normalizado

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}

df = pd.DataFrame(data)
df_nuevo = normalizar_min_max(df, ['A', 'B'])
print(df_nuevo)
