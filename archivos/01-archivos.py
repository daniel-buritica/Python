from pathlib import Path
from time import ctime
archivo = Path(r"C:\Users\burit\Documents\Backend\Python\archivos\archivos-prueba.txt")

# archivo.exists()
# archivo.rename()
# archivo.unlink() #eliminar el archivo

print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))