class Usuario():
    def guardar(self):
        print("guardando en db")

class Sesion():

    def guardar(self):
        print("guardando en archivo")


def guardar(entidades): #python no tiene tipado dinamico por defecto, lo que quiere decir que no validara si la entidad que recibe por el parametro extiende de model
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([usuario, sesion])
