class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela ave")


class Pato(Ave):
    def __init__(self):
        super().__init__()

    def vuela(self):
        super().vuela()
        return print("vuela pato")


pato = Pato()
pato.vuela()
