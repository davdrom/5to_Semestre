#Romero Ramos David
#952
#16/08/2023


"""
Dado una lista de números enteros y un valor entero (target), retorna el índice de los dos números que sumados sean
igual al target. Debe asumir que existe siempre una única solución, y que los elementos no se pueden usar dos veces.
Debes retornar una tupla con los índices.
"""
def busquedaSuma(nums, target):
    indices = {}
    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in indices:
            return indices[complemento], i
        indices[num] = i

print(busquedaSuma([2, 7, 11, 15], 9))
print(busquedaSuma([3, 2, 4], 6))
