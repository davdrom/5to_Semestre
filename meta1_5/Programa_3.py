def repetidos(lista):
    numRepetidos = 0
    for n in lista:
        if lista.count(n) >= 2:
            numRepetidos +=1
    sinRepetir = len(lista) - numRepetidos
    tupla = (sinRepetir, numRepetidos)
    return tupla

l = [1, 3, 1, 4, 5, 3, 7]
r = repetidos(l)
print(r)

l2 = [1, 3, 1, 1, 3, 4]
r2 = repetidos(l2)
print(r2)