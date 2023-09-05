for numero in range(5):
    print(numero)
    print(numero * numero)

buscar = 10
for numero in range(5):
    if numero == buscar:
        print("El número es: ", numero)
        break
else:
    print("no encontre el número buscado")


for char in "Ultimate python":
    print(char)
