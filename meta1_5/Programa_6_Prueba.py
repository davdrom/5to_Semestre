from Programa_6 import *

ruta = "C:/Users/romer.D-PC/PycharmProjects/ProgramacionFuncional/5to_Semestre/meta1_4/amazon_product_info.csv"
csv = LectorCSV(ruta)

print(csv.primeras_lineas(6))
print(csv.ultimas_lineas(7))
print(csv.aleatorio_lineas(8))
print(csv.nombres_columnas)
print(csv.tipos_datos_columnas)
print(csv.dimensiones_dataframe)