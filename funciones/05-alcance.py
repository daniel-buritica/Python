saludo = "Hola global"


def saludar():
    global saludo
    saludo = "Esto es a"
    print(saludo)


def saludar2():
    saludo = "Hola"
    print(saludo)


saludar()
saludar2()
