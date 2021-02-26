from Pymagochi import Pymagochi
from tkinter import * # importa a biblioteca
from random import randint

pymagochi = Pymagochi() # inicia o objeto tamagochi

## Funções de Event Handler
def alimentar():
    pymagochi.aumentaComida(randint(1,5))
    lComidaStatus['text'] = pymagochi.comida

def darBebida():
    pymagochi.aumentaBebida(randint(2,8))
    lBebidaStatus['text'] = pymagochi.bebida

def brincar():
    pymagochi.aumentaFelicidade(randint(1,8))
    lFelicidadeStatus['text'] = pymagochi.felicidade

def energia():
    pymagochi.aumentaEnergia(randint(1,5))
    lEnergiaStatus['text'] = pymagochi.energia

def banheiro():
    pymagochi.aumentaBanheiro(randint(8,10))
    lBanheiroStatus['text'] = pymagochi.banheiro


janela = Tk() # inicializa uma janela com base nas definições da biblioteca
janela.geometry("1000x700")#define as dimensões da janela

frame1 = Frame(janela)
frame1.pack(side=BOTTOM)

k= PhotoImage(file = "teste.png")

lImagem = Label(janela, image = k)
lImagem.pack()


lComida = Label(frame1, text="Comida")
lComida.grid(row = 0, column = 0)
lComidaStatus = Label(frame1, text=pymagochi.comida)
lComidaStatus.grid(row = 1, column = 0)
bComida = Button(frame1,text = "Alimentar", command = lambda: alimentar())
bComida.grid(row = 2, column = 0)

lBebida = Label(frame1, text="Bebida")
lBebida.grid(row = 0, column = 1)
lBebidaStatus = Label(frame1, text=pymagochi.bebida)
lBebidaStatus.grid(row = 1, column = 1)
bBebida = Button(frame1,text = "Bebida", command = lambda: darBebida())
bBebida.grid(row = 2, column = 1)

lFelicidade = Label(frame1, text="Felicidade")
lFelicidade.grid(row = 0, column = 2)
lFelicidadeStatus = Label(frame1, text=pymagochi.felicidade)
lFelicidadeStatus.grid(row = 1, column = 2)
bFelicidade = Button(frame1,text = "Brincar" , command = lambda: brincar())
bFelicidade.grid(row = 2, column = 2)

lEnergia = Label(frame1, text="Energia")
lEnergia.grid(row = 0, column = 3)
lEnergiaStatus = Label(frame1, text=pymagochi.energia)
lEnergiaStatus.grid(row = 1, column = 3)
bEnergia = Button(frame1,text = "Dormir", command = lambda: energia())
bEnergia.grid(row = 2, column = 3)

lBanheiro = Label(frame1, text="Banheiro")
lBanheiro.grid(row = 0, column = 4)
lBanheiroStatus = Label(frame1, text=pymagochi.banheiro)
lBanheiroStatus.grid(row = 1, column = 4)
bBanheiro = Button(frame1,text = "Banheiro" , command = lambda: banheiro())
bBanheiro.grid(row = 2, column = 4)

janela.mainloop()#inicia a janela




