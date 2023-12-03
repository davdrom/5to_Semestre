#Romero Ramos David 952
import pandas as pd

"""
Elimina los renglones repetidos de un DataFrame.
"""
def eliminar_renglones_repetidos(df):

    cantidad_renglones_original = len(df)
    df_nuevo = df.drop_duplicates()
    cantidad_renglones_nuevo = len(df_nuevo)
    cantidad_eliminados = cantidad_renglones_original - cantidad_renglones_nuevo

    return cantidad_eliminados, df_nuevo

data = {
    'A': [1, 2, 3, 1, 2],
    'B': ['a', 'b', 'c', 'a', 'b'],
    'C': [10, 20, 30, 10, 20]
}

df = pd.DataFrame(data)

cantidad_eliminados, df_nuevo = eliminar_renglones_repetidos(df)

print(f"\nSe eliminaron {cantidad_eliminados} renglones duplicados.")
print(df_nuevo)
