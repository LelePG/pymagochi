from threading import Timer

class Temporizador():

    def __init__(self, tempo_decremento, funcao_callback):
        self.tempo_decremento = tempo_decremento #id da thread
        self.funcao_callback = funcao_callback #funcao que será executada
        self.thread = Timer(self.tempo_decremento, self.roda_funcao) #Cria o temporizador

    def roda_funcao(self): # Para selecionar e rodar a função, é assim mesmo
        self.funcao_callback() #declara a função
        self.thread = Timer(self.tempo_decremento, self.roda_funcao) #cria a thread que vai rodar a função
        self.thread.start() #inicia a execução

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()