numeros = [1, 2, 3, 4, 5]

primero, segundo, tercero, cuarto, quinto = numeros

print(primero, segundo, tercero)

primero, *otros = numeros
print(primero, otros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

primero, *otros, ultimo = numeros
print(primero, otros, ultimo)
