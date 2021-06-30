from Pymagochi import Pymagochi
from Temporizador import Temporizador
from manipulador_interface import altera_valores as av
from tkinter import * # importa a biblioteca gráfica


## Variáveis

pymagochi = Pymagochi() # inicia o objeto tamagochi

janela = Tk() # inicializa uma janela com base nas definições da biblioteca
janela.geometry("600x350")#define as dimensões da janela

frame1 = Frame(janela) #cria o frame que compõe a janela
frame1.pack(side=BOTTOM)

status = { ## Objeto auxiliar para a criação da interface com os valores corretos.
    0:["Comida", "Alimentar", av.aumentar_comida, pymagochi.comida],
    1:["Bebida", "Beber", av.aumentar_bebida, pymagochi.bebida],
    2:["Felicidade", "Brincar", av.aumentar_felicidade, pymagochi.felicidade],
    3:["Energia", "Dormir", av.aumentar_energia, pymagochi.energia],
    4:["Banheiro", "Banheiro", av.aumentar_banheiro,pymagochi.banheiro],
}

## Funções de criação de elementos
def criar_label(titulo_label, linha, coluna):
    l = Label(frame1, text=titulo_label)
    l.grid(row = linha, column = coluna)
    return l

def criar_btn(texto_btn, funcao, linha, coluna):
    return Button(frame1,text = texto_btn, command = lambda: funcao(pymagochi)).grid(row = linha, column = coluna)

##Labels de estado
label_comida_status = criar_label(status[0][3],1,0)
label_bebida_status = criar_label(status[1][3],1,1)
label_felicidade_status = criar_label(status[2][3],1,2)
label_energia_status = criar_label(status[3][3],1,3)
label_banheiro_status = criar_label(status[4][3],1,4)

def atualizar_interface():
    label_comida_status['text'] = pymagochi.comida
    label_bebida_status['text'] = pymagochi.bebida
    label_felicidade_status['text'] = pymagochi.felicidade
    label_energia_status['text'] = pymagochi.energia
    label_banheiro_status['text'] = pymagochi.banheiro


k= PhotoImage(file = "teste.png") #Coloca a imagem na janela
lImagem = Label(janela, image = k)
lImagem.pack()

for i in range (len(status)): # cria a interface
    label_item = criar_label(status[i][0],0,i)
    btn_item = criar_btn(status[i][1], status[i][2], 2,i)

#Threads
atualiza_interface = Temporizador(0.5, atualizar_interface)
atualiza_interface.start()

##Falta: uma thread pra cada botão, verificar se o tamagochi morreu.

janela.mainloop()#inicia a janela
atualiza_interface.close()