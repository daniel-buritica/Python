class Animal:
    def comer(self):
        print("comiendo")


class Perro:
    def pasear(self):
        print("paseando")


class Gato(Animal, Perro):
    def maullar(self):
        print("maullando")


perro = Perro()
gato = Gato()


perro.pasear()

gato.comer()
gato.maullar()
gato.pasear()
