from io import open

# texto = "Hola Mundo"
# archivo = open(r"C:/Users/burit/Documents/Backend/Python/archivos/hola-mundo.txt", "w")
#
# archivo.write(texto)
# archivo.close()
#
# archivo = open(r"C:/Users/burit/Documents/Backend/Python/archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

with open(r"C:/Users/burit/Documents/Backend/Python/archivos/hola-mundo.txt", "r") as archivo: #Abre y cierra el archivo cuando lo utiliza
    print(archivo.readlines())
    archivo.seek(0) #devuelve el puntero a la posición que se le indique
    for linea in archivo:
        print(linea)