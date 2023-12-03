#Romero Ramos David 952

import pandas as pd

"""
Normaliza los datos de las columnas especificadas utilizando el escalado simple.
"""
def normalizar_datos_escalado_simple(df, columnas_a_normalizar):
    columnas_validas = set(columnas_a_normalizar)
    columnas_no_validas = columnas_validas - set(df.columns)
    if columnas_no_validas:
        raise ValueError(f"Las columnas {columnas_no_validas} no existen en el DataFrame")

    df_normalizado = df.copy()
    for columna in columnas_a_normalizar:
        max_valor = df_normalizado[columna].max()
        df_normalizado[columna] = df_normalizado[columna] / max_valor

    return df_normalizado

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}

df = pd.DataFrame(data)
df_nuevo = normalizar_datos_escalado_simple(df, ['A', 'B'])
print(df_nuevo)