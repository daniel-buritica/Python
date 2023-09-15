class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} ladro, y tiene {self.edad}")


print(Perro.patas)
Perro.patas = 2
mi_perro = Perro("luna", 25)
mi_perro2 = Perro("Luno", 20)
mi_perro2.patas = 9

print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
