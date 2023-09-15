class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} ladro, y tiene {self.edad}")


mi_perro = Perro("luna", 25)

mi_perro.habla()
