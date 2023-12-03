# Romero Ramos David 952
import pandas as pd

"""
Normaliza los datos de las columnas especificadas utilizando la técnica Z-Score.
"""
def normalizar_datos_z_score(df, columnas):


    columnas_validas = set(columnas)
    columnas_no_validas = columnas_validas - set(df.columns)
    if columnas_no_validas:
        raise ValueError(f"Las columnas {columnas_no_validas} no existen en el DataFrame")

    df_normalizado = df.copy()

    for columna in columnas:
        mean = df_normalizado[columna].mean()
        std = df_normalizado[columna].std()
        df_normalizado[columna] = (df_normalizado[columna] - mean) / std

    return df_normalizado

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}

df = pd.DataFrame(data)
df_nuevo = normalizar_datos_z_score(df, ['A', 'B'])
print(df_nuevo)
