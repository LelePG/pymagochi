import threading
import os

class minhaThread(threading.Thread):
    def __init__(self, tempo_atualizacao, funcao_callback):
        threading.Thread.__init__(self)
        self.tempo_atualizacao = tempo_atualizacao
        self.funcao_callback = funcao_callback

    def roda_funcao(self): # Para selecionar e rodar a função, é assim mesmo
        try:
            self.funcao_callback() #declara a função
            self.thread = threading.Timer(self.tempo_atualizacao, self.roda_funcao) #cria a thread que vai rodar a função
            self.thread.start() #inicia a execução
        except: # se contecer algum problema, fecha o programa.
            self.thread.cancel()
            os._exit(1)



