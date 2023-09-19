class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):
    def pasear(self):
        print("paseando")


class Gato(Animal):
    def maullar(self):
        print("maullando")


perro = Perro()
gato = Gato()

perro.comer()
perro.pasear()

gato.comer()
gato.maullar()
