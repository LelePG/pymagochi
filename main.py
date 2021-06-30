from Pymagochi import Pymagochi
from Contador import Contador
from manipulador_interface import altera_valores as av
from tkinter import * # importa a biblioteca gráfica

## Funções de criação de elementos
def criar_label(titulo_label, linha, coluna):
    return Label(frame1, text=titulo_label).grid(row = linha, column = coluna)

def criar_label_status(texto_label, linha, coluna):
    return Label(frame1, text=texto_label).grid(row = linha, column = coluna)

def criar_btn(texto_btn, funcao, label_status, linha, coluna):
    return Button(frame1,text = texto_btn, command = lambda: atualizar_interface(funcao, label_status)).grid(row = linha, column = coluna)

pymagochi = Pymagochi() # inicia o objeto tamagochi

janela = Tk() # inicializa uma janela com base nas definições da biblioteca
janela.geometry("600x350")#define as dimensões da janela

frame1 = Frame(janela) #cria o frame que compõe a janela
frame1.pack(side=BOTTOM)

k= PhotoImage(file = "teste.png") #Coloca a imagem na janela
lImagem = Label(janela, image = k)
lImagem.pack()

status = { ## Objeto auxiliar para a criação da interface com os valores corretos.
    0:["Comida", "Alimentar", av.aumentar_comida, pymagochi.comida,0],
    1:["Bebida", "Beber", av.aumentar_bebida, pymagochi.bebida,0],
    2:["Felicidade", "Brincar", av.aumentar_felicidade, pymagochi.felicidade,0],
    3:["Energia", "Dormir", av.aumentar_energia, pymagochi.energia,0],
    4:["Banheiro", "Banheiro", av.aumentar_banheiro,pymagochi.banheiro,0],
}

label_comida_status = status[0][4]
label_bebida_status = status[1][4]
label_felicidade_status = status[2][4]
label_energia_status = status[3][4]
label_banheiro_status = status[4][4]

for i in range (len(status)-2):
    label_item = criar_label(status[i][0],0,i)
    status[i][4] = criar_label_status(status[i][3],1,i)
    btn_item = criar_btn(status[i][1], status[i][2], status[i][4], 2,i)



#label_comida = criar_label("Comida",0,0)
#label_comida_status = criar_label(pymagochi.comida,1,0)

# label_comida = Label(frame1, text="Comida")
# label_comida.grid(row = 0, column = 0)
# label_comida_status = Label(frame1, text=pymagochi.comida)
# label_comida_status.grid(row = 1, column = 0)
# btn_comida = Button(frame1,text = "Alimentar", command = lambda: aumentar_comida())
# btn_comida.grid(row = 2, column = 0)

# lBebida = Label(frame1, text="Bebida")
# lBebida.grid(row = 0, column = 1)
# lBebidaStatus = Label(frame1, text=pymagochi.bebida)
# lBebidaStatus.grid(row = 1, column = 1)
# bBebida = Button(frame1,text = "Bebida", command = lambda: aumentar_bebida())
# bBebida.grid(row = 2, column = 1)

# lFelicidade = Label(frame1, text="Felicidade")
# lFelicidade.grid(row = 0, column = 2)
# lFelicidadeStatus = Label(frame1, text=pymagochi.felicidade)
# lFelicidadeStatus.grid(row = 1, column = 2)
# bFelicidade = Button(frame1,text = "Brincar" , command = lambda: aumentar_felicidade())
# bFelicidade.grid(row = 2, column = 2)

# lEnergia = Label(frame1, text="Energia")
# lEnergia.grid(row = 0, column = 3)
# lEnergiaStatus = Label(frame1, text=pymagochi.energia)
# lEnergiaStatus.grid(row = 1, column = 3)
# bEnergia = Button(frame1,text = "Dormir", command = lambda: aumentar_energia())
# bEnergia.grid(row = 2, column = 3)

# lBanheiro = Label(frame1, text="Banheiro")
# lBanheiro.grid(row = 0, column = 4)
# lBanheiroStatus = Label(frame1, text=pymagochi.banheiro)
# lBanheiroStatus.grid(row = 1, column = 4)
# bBanheiro = Button(frame1,text = "Banheiro" , command = lambda: aumentar_banheiro())
# bBanheiro.grid(row = 2, column = 4)


janela.mainloop()#inicia a janela
