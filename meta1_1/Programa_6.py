#Romero Ramos David
#952
#16/08/2023

"""
Programa 6
"""


class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros

    def frecuenciaNumeros(self):
        freq = {}
        for num in self.numeros:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        return freq

    def moda(self):
        freq = self.frecuenciaNumeros()
        max_freq = max(freq.values())
        moda_valores = [num for num, frecuencia in freq.items() if frecuencia == max_freq]
        return moda_valores

    def histograma(self):
        freq = self.frecuenciaNumeros()
        for num, count in freq.items():
            print(f"{num} {'*' * count}")


numeros = [1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1]
estadistica = Estadistica(numeros)
estadistica.histograma()
