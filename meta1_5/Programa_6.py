import pandas as pd
import random
class LectorCSV:
    def __init__(self, ruta):
        self.ruta = ruta
        self.datos = pd.read_csv(ruta)

    def primeras_lineas(self, n):
        return self.datos.head(n)

    def ultimas_lineas(self, n):
        return self.datos.tail(n)

    def aleatorio_lineas(self, n):
        return self.datos.sample(n)

    @property
    def nombres_columnas(self):
        return self.datos.columns.tolist()

    @property
    def tipos_datos_columnas(self):
        return self.datos.dtypes.tolist()

    @property
    def dimensiones_dataframe(self):
        shape = self.datos.shape
        return (shape[0], shape[1])

