import random

listaOrdenada = [1,2,3,4,5,6,7]
listaOrdenada2 = [1,2,3,4,5,6,7]
random.shuffle(listaOrdenada) #des Ordenar lista
print(
    random.random(),
    random.randint(1,10),
    listaOrdenada,
    random.choice(listaOrdenada2),
    random.choices(listaOrdenada2, k=3)
)