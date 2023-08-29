animal = "chanchito feliz"
print(animal.upper());
print(animal.lower());
print(animal.capitalize()); ##nos da el primer caracter el mayuscula
print(animal.title()); ##nos da el string como titulo
print(animal.strip()); ##quita espacios a la derecha he izquierda del string
print(animal.lstrip()); ##quita espacios a la derecha
print(animal.rstrip()); ##quita espacios a la izquierda del string
print(animal.strip().capitalize()); ##encadenar metodos
print(animal.find("ch")); ##devuelve el el indice del string
print(animal.replace("ch", "d")); ##remplaza la cadena que se le paso
print("ch" in animal); ##devuelve un tru si encuentra la cadena o false si no la encuentra
print("ch" not in animal); ##devuelve un tru si encuentra la cadena o false si no la encuentra

