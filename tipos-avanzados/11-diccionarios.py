punto = {"x": 25, "y": 50}

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45  # asignar un nuevo atributo

print(punto)

if "lala" in punto:
    print("encontre lala")

print(punto.get("x"))
print(punto.get("lala", 97))

# eliminar un atributo

del punto["x"]
print(punto)

# llamar al diccionario por medio del form

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)
