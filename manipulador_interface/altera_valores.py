from random import randint

## Funções de Event Handler (ativadas com o botão)
def aumentar_comida(elemento, label):
    elemento.aumenta_comida(randint(1,5))
    label['text'] = elemento.comida

def aumentar_bebida(elemento,label):
    elemento.aumenta_bebida(randint(2,8))
    label['text'] = elemento.bebida

def aumentar_felicidade(elemento,label):
    elemento.aumenta_felicidade(randint(1,8))
    label['text'] = elemento.felicidade

def aumentar_energia(elemento,label):
    elemento.aumenta_energia(randint(1,5))
    label['text'] = elemento.energia

def aumentar_banheiro(elemento,label):
    elemento.aumenta_banheiro(randint(8,10))
    label['text'] =elemento.banheiro


## Funções de decremento dos valores padrão que serão instanciadas em threads
def diminuir_comida(elemento,label):
    elemento.diminui_comida(randint(1,5))
    label['text'] = elemento.comida

def diminuir_bebida(elemento,label):
    elemento.diminui_bebida(randint(2,8))
    label['text'] = elemento.bebida

def diminuir_felicidade(elemento,label):
    elemento.diminui_felicidade(randint(1,8))
    label['text'] = elemento.felicidade

def diminuir_energia(elemento,label):
    elemento.diminui_energia(randint(1,5))
    label['text'] = elemento.energia

def diminuir_banheiro(elemento,label):
    elemento.diminui_banheiro(randint(8,10))
    label['text'] = elemento.banheiro