import threading
from threading import Timer

class minhaThread (threading.Thread):
    def __init__(self, tempo_atualizacao, funcao_callback):
        threading.Thread.__init__(self)
        self.tempo_atualizacao = tempo_atualizacao
        self.funcao_callback = funcao_callback

    def roda_funcao(self): # Para selecionar e rodar a função, é assim mesmo
        self.funcao_callback() #declara a função
        self.thread = Timer(self.tempo_atualizacao, self.roda_funcao) #cria a thread que vai rodar a função
        self.thread.start() #inicia a execução

    # def run(self):
    #     print "Iniciando thread %s com %d processos" % (self.name,self.contador)
    #     processo(self.nome, self.contador)
    #     print "Finalizando " + self.nome

# def processo(nome, contador):
#     while contador:
#         print "Thread %s fazendo o processo %d" % (nome, contador)
#         contador -= 1

# # Criando as threads
# thread1 = minhaThread(1, "Alice", 8)
# thread2 = minhaThread(2, "Bob", 8)

# # Comecando novas Threads
# thread1.start()
# thread2.start()

# threads = []
# threads.append(thread1)
# threads.append(thread2)

# for t in threads:
#     t.join()

# print "Saindo da main"