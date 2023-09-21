from pathlib import Path
path = Path(r"C:\Users\burit\Downloads\mi-archivo.py")

path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("update-py")
print(p)
p = path.with_suffix(".exe")
print(p)