from Pymagochi import Pymagochi
from Contador import Contador
from tkinter import * # importa a biblioteca gráfica
from random import randint


pymagochi = Pymagochi() # inicia o objeto tamagochi

## Funções de Event Handler (ativadas com o botão)
def aumentar_comida():
    pymagochi.aumenta_comida(randint(1,5))
    label_comida_status['text'] = pymagochi.comida

def aumentar_bebida():
    pymagochi.aumenta_bebida(randint(2,8))
    label_bebida_status['text'] = pymagochi.bebida

def aumentar_felicidade():
    pymagochi.aumenta_felicidade(randint(1,8))
    label_felicidade_status['text'] = pymagochi.felicidade

def aumentar_energia():
    pymagochi.aumenta_energia(randint(1,5))
    label_energia_status['text'] = pymagochi.energia

def aumentar_banheiro():
    pymagochi.aumenta_banheiro(randint(8,10))
    label_banheiro_status['text'] = pymagochi.banheiro


## Funções de decremento dos valores padrão que serão instanciadas em threads
def diminuir_comida():
    pymagochi.diminui_comida(randint(1,5))
    label_comida_status['text'] = pymagochi.comida

def diminuir_bebida():
    pymagochi.diminui_bebida(randint(2,8))
    label_bebida_status['text'] = pymagochi.bebida

def diminuir_felicidade():
    pymagochi.diminui_felicidade(randint(1,8))
    label_felicidade_status['text'] = pymagochi.felicidade

def diminuir_energia():
    pymagochi.diminui_energia(randint(1,5))
    label_energia_status['text'] = pymagochi.energia

def diminuir_banheiro():
    pymagochi.diminui_banheiro(randint(8,10))
    label_banheiro_status['text'] = pymagochi.banheiro


janela = Tk() # inicializa uma janela com base nas definições da biblioteca
janela.geometry("600x350")#define as dimensões da janela

frame1 = Frame(janela) #cria a janela
frame1.pack(side=BOTTOM)

k= PhotoImage(file = "teste.png") #Coloca a imagem na janela
lImagem = Label(janela, image = k)
lImagem.pack()
   
label_comida = Label(frame1, text="Comida")
label_comida.grid(row = 0, column = 0)
label_comida_status = Label(frame1, text=pymagochi.comida)
label_comida_status.grid(row = 1, column = 0)
btn_comida = Button(frame1,text = "Alimentar", command = lambda: aumentar_comida())
btn_comida.grid(row = 2, column = 0)

lBebida = Label(frame1, text="Bebida")
lBebida.grid(row = 0, column = 1)
lBebidaStatus = Label(frame1, text=pymagochi.bebida)
lBebidaStatus.grid(row = 1, column = 1)
bBebida = Button(frame1,text = "Bebida", command = lambda: aumentar_bebida())
bBebida.grid(row = 2, column = 1)

lFelicidade = Label(frame1, text="Felicidade")
lFelicidade.grid(row = 0, column = 2)
lFelicidadeStatus = Label(frame1, text=pymagochi.felicidade)
lFelicidadeStatus.grid(row = 1, column = 2)
bFelicidade = Button(frame1,text = "Brincar" , command = lambda: aumentar_felicidade())
bFelicidade.grid(row = 2, column = 2)

lEnergia = Label(frame1, text="Energia")
lEnergia.grid(row = 0, column = 3)
lEnergiaStatus = Label(frame1, text=pymagochi.energia)
lEnergiaStatus.grid(row = 1, column = 3)
bEnergia = Button(frame1,text = "Dormir", command = lambda: aumentar_energia())
bEnergia.grid(row = 2, column = 3)

lBanheiro = Label(frame1, text="Banheiro")
lBanheiro.grid(row = 0, column = 4)
lBanheiroStatus = Label(frame1, text=pymagochi.banheiro)
lBanheiroStatus.grid(row = 1, column = 4)
bBanheiro = Button(frame1,text = "Banheiro" , command = lambda: aumentar_banheiro())
bBanheiro.grid(row = 2, column = 4)


janela.mainloop()#inicia a janela
