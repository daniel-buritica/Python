numeros = (1, 2, 3) + (4, 5, 6)

print(numeros)


punto = tuple([1, 2, 3])

print(punto)

acceso = numeros[:4]
print(acceso)

primero, segundo, *otros = numeros

print(primero, segundo, otros)

listaNumeros = list(numeros)
print(listaNumeros)
