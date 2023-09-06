def hola(nombre, apellido):
    print("hola mundo")
    print(f"ultima python {nombre} {apellido}")


hola("Daniel", "buritica")


def hola2(nombre, apellido="feliz"):  # Argumentos con valor por defecto
    print("hola mundo")
    print(f"ultima python {nombre} {apellido}")


# para identificar los argumentos que se pasan a la funcion
hola(apellido="junco", nombre="daniel")
