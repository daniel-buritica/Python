from pathlib import Path

path = Path(r"C:\Users\burit\Documents\Backend\Python\rutas")
# path.exists()
# path.mkdir()
# path.rmdir() #sirve para eliminar directorios siempre y cuando esten vaciosp
# #path.rename("update-directorio")

for p in path.iterdir():
    print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos2 = [p for p in path.glob("01-*.py")]
archivos3 = [p for p in path.glob("**/*.py")]

print(archivos)
print(archivos2)
print(archivos3)


