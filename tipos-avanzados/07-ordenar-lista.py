list_numbers = [3, 4, 6, 3, 1, 2]
list_numbers.sort(reverse=True)
list_numbers.sort()

print(list_numbers)


numbers = sorted(list_numbers)  # Crear una lista nueva

print(numbers)

usuarios = [[1, "daniel"], [2, "kevin"]]

usuarios.sort(reverse=True)

print(usuarios)


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena, reverse=False)
# podemos remplazar la funcion por un lamda
usuarios.sort(key=lambda el: el[1])


print(usuarios)
