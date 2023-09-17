#Romero Ramos David
#952
#16/08/2023


"""
ENCRIPTAR Y DESENCRIPTAR
"""

def encripta(mensaje, clave):
    mensaje_encriptado = []
    for caracter in mensaje:
        if caracter.isalpha():
            indice = ord(caracter) - ord('a')
            caracter_encriptado = clave[indice]
            mensaje_encriptado.append(caracter_encriptado)
        else:
            mensaje_encriptado.append(caracter)
    return ''.join(mensaje_encriptado)

def desencripta(mensaje_encriptado, clave):
    mensaje_desencriptado = []
    for caracter in mensaje_encriptado:
        if caracter.isalpha():
            indice = clave.index(caracter)
            caracter_desencriptado = chr(indice + ord('a'))
            mensaje_desencriptado.append(caracter_desencriptado)
        else:
            mensaje_desencriptado.append(caracter)
    return ''.join(mensaje_desencriptado)

clave = 'ixmrklstnuzbowfaqejdcpvhyg'

mensaje1 = 'cafe'
mensaje2 = 'dame 1 chocolate'

mensaje1_encriptado = encripta(mensaje1, clave)
mensaje2_encriptado = encripta(mensaje2, clave)

print(mensaje1_encriptado)
print(mensaje2_encriptado)

mensaje1_desencriptado = desencripta(mensaje1_encriptado, clave)
mensaje2_desencriptado = desencripta(mensaje2_encriptado, clave)

print(mensaje1_desencriptado)
print(mensaje2_desencriptado)
