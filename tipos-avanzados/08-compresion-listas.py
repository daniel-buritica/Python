usuarios = [[1, "daniel"], [2, "kevin"]]
print(usuarios)
nombres = []
for usuario in usuarios:
    nombres.append(usuario[1])

print(nombres)

nombres2 = [usuario[1] for usuario in usuarios]
print(nombres2)
# filtrar

nombres3 = [usuario[0] for usuario in usuarios if usuario[0] > 1]
print(nombres3)
# transformar lista
result = list(map(lambda usuario: usuario[0], usuarios))
print("map:", result)
# filtrar lista
result2 = list(filter(lambda usuario: usuario[0] > 1, usuarios))

print("filter: ", result)
