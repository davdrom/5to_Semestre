def divisible5(lista):
    resultados = []
    for i in lista:
        if i % 5 == 0:
            resultados.append(True)
        else:
            resultados.append(False)
    return resultados

lista = [10,3,5,9,15,1]

d = divisible5(lista)
print(d)