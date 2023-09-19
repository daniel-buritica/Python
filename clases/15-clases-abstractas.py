from abc import ABC, abstractclassmethod


class Model(ABC):

    def __init__(self):
        if not self.tabla:
            print("Tienes que definir una tabla")

    @property
    @abstractclassmethod
    def tabla(self):
        pass

    @abstractclassmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id: {_id}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print(f"Guardando: {self.tabla} en db ")


usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(2)
