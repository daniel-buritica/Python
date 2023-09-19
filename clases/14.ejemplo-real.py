class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando: {self.tabla} en db ")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id: {_id}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(2)
