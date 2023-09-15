class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Gua ")

    @classmethod
    def factory(cls):
        return cls("luna", 20)


Perro.habla()
mi_perro = Perro("luno", 10)
mi_perro2 = Perro.factory()

print(mi_perro)
print(mi_perro2.edad, mi_perro2.nombre)
