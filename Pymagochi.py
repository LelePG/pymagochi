class Pymagochi:
    # Status
    comida = 0
    bebida = 0
    felicidade = 0
    energia = 0
    banheiro = 0
    coco = False

    #Funções para alterar os estatos
    def aumentaComida(self, valorAumento):
        self.comida += valorAumento
        if self.comida > 10:
            self.comida = 10
        return

    def diminuiComida(self, valorAumento):
        self.comida -= valorAumento
        if self.comida < 0:
            self.comida = 0
        return

    def aumentaBebida(self, valorAumento):
        self.bebida += valorAumento
        if self.bebida > 10:
            self.bebida = 10
        return

    def diminuiBebida(self, valorAumento):
        self.bebida -= valorAumento
        if self.bebida < 0:
            self.bebida = 0
        return

    def aumentaFelicidade(self, valorAumento):
        self.felicidade += valorAumento
        if self.felicidade > 10:
            self.felicidade = 10
        return

    def diminuiFelicidade(self, valorAumento):
        self.felicidade -= valorAumento
        if self.felicidade < 0:
            self.felicidade = 0
        return

    def aumentaEnergia(self, valorAumento):
        self.energia += valorAumento
        if self.energia > 10:
            self.energia = 10
        return

    def diminuiEnergia(self, valorAumento):
        self.energia -= valorAumento
        if self.energia < 0:
            self.energia = 0
        return

    def aumentaBanheiro(self, valorAumento):
        self.banheiro += valorAumento
        if self.banheiro > 10:
            self.banheiro = 10
        return

    def diminuiBanheiro(self, valorAumento):
        self.banheiro -= valorAumento
        if self.banheiro < 0:
            self.ebanheiro = 0
        return

    # Funções de display de status
    def displayComida(self):
        text = ""
        for c in range (self.comida):
            text += "*"
            #print(text)
        return text





    def mostraStatus(self):
        print(f'Comida: {self.comida}')
        print(f'Bebida: {self.bebida}')
        print(f'Felicidade: {self.felicidade}')
        print(f'Energia: {self.energia}')
        print("-----------------")

