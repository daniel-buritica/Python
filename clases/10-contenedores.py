class Productos:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nomnre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


balon = Productos("Balon", 100)
tenis = Productos("Tenis Futbol", 300)
uniforme = Productos("Uniforme Futbol", 250)

deporte = Categoria("Deportes", [balon, tenis])
deporte.agregar(uniforme)

deporte.imprimir()
