from Pymagochi import Pymagochi
from manipulador_interface import altera_valores as av
from manipulador_interface import cria_threads as ct
from manipulador_interface import cria_elementos as ce
from tkinter import * # importa a biblioteca gráfica
from tkinter import messagebox
from random import randint
import time

# constantes
TEMPO_ATUALIZAR_INTERFACE = 0.25
TEMPO_DECREMENTAR_STATUS = 0.5
TEMPO_VISUALIZA_CAIXA = 5

## Variáveis do programa
pymagochi = Pymagochi("teste.png") # inicia o objeto tamagochi

janela = Tk() # inicializa uma janela com base nas definições da biblioteca
janela.geometry("600x350")#define as dimensões da janela

frame_principal = Frame(janela) #cria o frame que compõe a janela
frame_principal.pack(side=BOTTOM)

pymagochi_foto = PhotoImage(file = pymagochi.imagem) #Coloca a imagem na janela
label_imagem = Label(janela, image  = pymagochi_foto)
label_imagem.pack()

status = { ## Map auxiliar para a criação da interface com os valores corretos.
    0:["Comida", "Alimentar", av.aumentar_comida, pymagochi.comida],
    1:["Bebida", "Dar água", av.aumentar_bebida, pymagochi.bebida],
    2:["Felicidade", "Brincar", av.aumentar_felicidade, pymagochi.felicidade],
    3:["Energia", "Dormir", av.aumentar_energia, pymagochi.energia],
    4:["Banheiro", "Banheiro", av.aumentar_banheiro,pymagochi.banheiro],
}

##Labels de estado
label_comida_status = ce.criar_label(frame_principal,status[0][3],1,0)
label_bebida_status = ce.criar_label(frame_principal,status[1][3],1,1)
label_felicidade_status = ce.criar_label(frame_principal,status[2][3],1,2)
label_energia_status = ce.criar_label(frame_principal,status[3][3],1,3)
label_banheiro_status = ce.criar_label(frame_principal,status[4][3],1,4)


def monitorar_interface():
    if not pymagochi.esta_vivo():
        messagebox.showwarning("RIP", "Você deixou o Pymagochi morrer")# mostra mensagem de erro
        janela.destroy()
    elif pymagochi.banheiro_zerado():
        messagebox.showwarning("Aconteceu um acidente", "Limpe a caixa de areia do pymagochi")
        pymagochi.banheiro = 10
        time.sleep(TEMPO_VISUALIZA_CAIXA)

def atualizar_interface():
    label_comida_status['text'] = pymagochi.comida
    label_bebida_status['text'] = pymagochi.bebida
    label_felicidade_status['text'] = pymagochi.felicidade
    label_energia_status['text'] = pymagochi.energia
    label_banheiro_status['text'] = pymagochi.banheiro   

def decrementar_status(): # eu queria utilizar um switch, mas não tem em python
    status_dec = randint(0,4)
    if status_dec == 0:
        av.diminuir_comida(pymagochi)
    elif status_dec == 1:
        av.diminuir_bebida(pymagochi)
    elif status_dec == 2:
        av.diminuir_felicidade(pymagochi)
    elif status_dec == 3:
        av.diminuir_energia(pymagochi)
    elif status_dec == 4:
        av.diminuir_banheiro(pymagochi)
    else:
        print("Problema encontrado")
    monitorar_interface()


for i in range (len(status)): # cria a interface
    label_item = ce.criar_label(frame_principal,status[i][0],0,i)
    btn_item = ce.criar_btn(frame_principal,pymagochi,status[i][1], status[i][2], 2,i)


ct.minhaThread(TEMPO_ATUALIZAR_INTERFACE, atualizar_interface).roda_funcao()
ct.minhaThread(TEMPO_DECREMENTAR_STATUS, decrementar_status).roda_funcao()

janela.mainloop()#inicia a janela


    
