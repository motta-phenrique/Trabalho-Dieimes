class Cabeca:
    def _init_(self):
        self.estado = "Intacta"

    def destruir(self):
        self.estado = "Destruída"
        print("A cabeça foi destruída!")

class Boneco:
    def _init_(self):
        self.cabeca = Cabeca()

    def destruir(self):
        self.cabeca.destruir()
        print("O boneco foi destruído!")

if _name_ == "_main_":
    boneco = Boneco()
    boneco.destruir()