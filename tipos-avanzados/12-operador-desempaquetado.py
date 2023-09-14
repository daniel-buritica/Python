lista1 = [1, 2, 3, 4]
print(*lista1)

lista2 = [7, 8, 9]

combinada = ["holal", *lista1, "hola2", lista2]
print(combinada)

punto1 = {"x": 1}
punto2 = {"y": 2}

nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
