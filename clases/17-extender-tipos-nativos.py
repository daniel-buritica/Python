class Lista(list):
    def prepend(self, item):
        self.insert(0, item)

lista = Lista([1,2,3])
lista.append(5)
lista.prepend(0)
print(lista)