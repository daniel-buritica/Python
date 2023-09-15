class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.__nombre} dice : GuaU! ")

    def get_nombre(self):
        return self.__nombre

    @classmethod
    def factory(cls):
        return cls("luna", 20)


mi_perro = Perro.factory()

print(mi_perro.get_nombre())
print(mi_perro.__dict__)
