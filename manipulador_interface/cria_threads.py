import threading
from threading import Timer

class minhaThread(threading.Thread):
    def __init__(self, tempo_atualizacao, funcao_callback):
        threading.Thread.__init__(self)
        self.tempo_atualizacao = tempo_atualizacao
        self.funcao_callback = funcao_callback

    def roda_funcao(self): # Para selecionar e rodar a função, é assim mesmo
        self.funcao_callback() #declara a função
        self.thread = Timer(self.tempo_atualizacao, self.roda_funcao) #cria a thread que vai rodar a função
        self.thread.start() #inicia a execução
