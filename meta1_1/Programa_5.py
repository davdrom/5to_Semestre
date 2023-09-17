#Romero Ramos David
#952
#16/08/2023

"""
Programa 5
"""

class Pensionista:
    def __init__(self, identificador, edad, gastos, nombre):
        self.identificador = identificador
        self.edad = edad
        self.gastos = gastos
        self.nombre = nombre


class GrupoPensionistas:
    def __init__(self, pensionistas):
        self.pensionistas = pensionistas

    def mediaGastos(self, identificador):
        pensionista = self.pensionistas[identificador]
        return sum(pensionista.gastos) / len(pensionista.gastos)

    def mediaEdad(self):
        return sum(p.edad for p in self.pensionistas) / len(self.pensionistas)

    def edadesExtremas(self):
        min_p = min(self.pensionistas, key=lambda p: p.edad)
        max_p = max(self.pensionistas, key=lambda p: p.edad)
        return min_p, max_p

    def sumaPromedio(self):
        return sum(sum(p.gastos) / len(p.gastos) for p in self.pensionistas)

    def mediaMaxima(self):
        max_p = max(self.pensionistas, key=lambda p: sum(p.gastos) / len(p.gastos))
        return sum(max_p.gastos) / len(max_p.gastos), max_p.nombre, max_p.identificador

    def gastoPromedio(self):
        return sorted([sum(p.gastos) / len(p.gastos) for p in self.pensionistas])


pensionistas = [
    Pensionista('1111A', 68, [640, 589, 573], 'Carlos'),
    Pensionista('2222B', 75, [700, 800], 'Elena')
]

grupo = GrupoPensionistas(pensionistas)
print(grupo.mediaGastos(0))
print(grupo.mediaEdad())
print(grupo.edadesExtremas())
print(grupo.sumaPromedio())
print(grupo.mediaMaxima())
print(grupo.gastoPromedio())
