#Romero Ramos David
#952
import pandas as pd

df = pd.read_csv('titanic.csv')

print("Dimensiones del DataFrame:")
print(df.shape)  # Filas, Columnas

print("\nInformacion sobre el DataFrame:")
print(df.info())

print("\nPrimeras 10 filas:")
print(df.head(10))
print("\nUltimas 10 filas:")
print(df.tail(10))

sobrevivieron = df['Survived'].value_counts(normalize=True) * 100 # Calcula el porcentaje de personas que sobrevivieron y murieron, normalizado a valores de 0 a 100
print("\nPorcentaje de personas que sobrevivieron y murieron:")
print(sobrevivieron)

sobrevivieron_por_clase = df.groupby('Pclass')['Survived'].mean() * 100
print("\nPorcentaje de personas que sobrevivieron en cada clase:")
print(sobrevivieron_por_clase)
