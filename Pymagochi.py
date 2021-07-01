class Pymagochi:
    # Status
    comida = 10
    bebida = 10
    felicidade = 10
    energia = 10
    banheiro = 10
    coco = False
    

    def __init__(self,imagem):
        self.imagem = imagem

    #Funções para alterar os estatos
    def aumenta_comida(self, valorAumento):
        self.comida += valorAumento
        if self.comida > 10:
            self.comida = 10
        

    def diminui_comida(self, valorAumento):
        self.comida -= valorAumento
        if self.comida < 0:
            self.comida = 0
        

    def aumenta_bebida(self, valorAumento):
        self.bebida += valorAumento
        if self.bebida > 10:
            self.bebida = 10
        

    def diminui_bebida(self, valorAumento):
        self.bebida -= valorAumento
        if self.bebida < 0:
            self.bebida = 0
        

    def aumenta_felicidade(self, valorAumento):
        self.felicidade += valorAumento
        if self.felicidade > 10:
            self.felicidade = 10
        

    def diminui_felicidade(self, valorAumento):
        self.felicidade -= valorAumento
        if self.felicidade < 0:
            self.felicidade = 0
        

    def aumenta_energia(self, valorAumento):
        self.energia += valorAumento
        if self.energia > 10:
            self.energia = 10
        

    def diminui_energia(self, valorAumento):
        self.energia -= valorAumento
        if self.energia < 0:
            self.energia = 0
        

    def aumenta_banheiro(self, valorAumento):
        self.banheiro += valorAumento
        if self.banheiro > 10:
            self.banheiro = 10
        

    def diminui_banheiro(self, valorAumento):
        self.banheiro -= valorAumento
        if self.banheiro < 0:
            self.banheiro = 0
        
    #monitoramento
    def esta_vivo(self):
        return self.comida and self.bebida and self.energia and self.felicidade # Não considera o banheiro

    def banheiro_zerado(self):
        return self.banheiro == 0

    def mostraStatus(self): #debug
        print(f'Comida: {self.comida}')
        print(f'Bebida: {self.bebida}')
        print(f'Felicidade: {self.felicidade}')
        print(f'Energia: {self.energia}')
        print(f'Banheiro: {self.banheiro}')
        print("-----------------")

