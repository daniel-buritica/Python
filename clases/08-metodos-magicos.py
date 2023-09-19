class Perro:  # Los metodos magicos son los que se ejecutan sin necesidad de llamarlos

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):  # Se ejecuta cuando se elimina una isntacia del objeto perro
        print(f"{self.nombre} fue eliminado:C")

    def __str__(self):
        return f"Clase perro : {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice : Gua")


perro = Perro("Luna", 7)

print(perro.edad, perro.nombre, perro)

del perro
