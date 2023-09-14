# set significa clase o conjunto, coleccion de datos que no se puede repetir ni tampoco esta ordenada


primero = {1, 1, 2, 3, 4, 5}

print(primero)

primero.add(5)
primero.remove(1)

print(primero)

segundo = [3, 4, 5, 9]

segundo = set(segundo)

print(segundo)

print(primero | segundo)
