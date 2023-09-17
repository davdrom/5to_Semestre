#Romero Ramos David
#952
import pandas as pd

def cotizaciones(nom_archivo):
    df = pd.read_csv(nom_archivo, sep=";", decimal=",")

    resumen = {
        'Mínimo': df.min(),
        'Máximo': df.max(),
        'Media': df.mean()
    }

    df_resumen = pd.DataFrame(resumen)
    return df_resumen


nom_archivo = 'cotizacion.csv'

df_resumen = cotizaciones(nom_archivo)

print(df_resumen)
