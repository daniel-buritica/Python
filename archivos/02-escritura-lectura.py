from pathlib import Path
from time import ctime
archivo = Path(r"C:\Users\burit\Documents\Backend\Python\archivos\archivos-prueba.txt")

texto = archivo.read_text("utf-8").split("\n")
texto.insert(0, "Hola mundo")
archivo.write_text("\n".join(texto),"utf-8")
print(texto)