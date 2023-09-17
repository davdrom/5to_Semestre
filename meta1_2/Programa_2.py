#Romero Ramos David
#952
import pandas as pd

def calcular_balance(dataframe, meses):

    filtro = dataframe[dataframe['Mes'].isin(meses)]
    balance_total = (filtro['Ventas'] - filtro['Gastos']).sum()
    return balance_total

datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas': [30500, 35600, 28300, 33900],
    'Gastos': [22000, 23400, 18100, 20700]
}

df = pd.DataFrame(datos)

p1 = ['Enero']
p2 = ['Enero', 'Febrero', 'Marzo', 'Abril']

calcular_balance(df, p1)
print(f"Balance total: ${calcular_balance(df, p1)}")
print(f"Balance total: ${calcular_balance(df, p2)}")

