from random import randint
from Pymagochi import Pymagochi


def definir_entidade(entidade):
    elemento_principal = entidade

## Funções de Event Handler (ativadas com o botão)
def aumentar_comida(elemento):
    Pymagochi.aumenta_comida(elemento,randint(1,5))

def aumentar_bebida(elemento):
    Pymagochi.aumenta_bebida(elemento, randint(2,8))
    

def aumentar_felicidade(elemento):
    Pymagochi.aumenta_felicidade(elemento, randint(1,8))
    

def aumentar_energia(elemento):
    Pymagochi.aumenta_energia(elemento, randint(1,5))
   

def aumentar_banheiro(elemento):
    Pymagochi.aumenta_banheiro(elemento, randint(8,10))
    

## Funções de decremento dos valores padrão que serão instanciadas em threads
def diminuir_comida(elemento):
    Pymagochi.diminui_comida(elemento, randint(1,3))
    

def diminuir_bebida(elemento):
   Pymagochi.diminui_bebida(elemento, randint(1,3))
    

def diminuir_felicidade(elemento):
   Pymagochi.diminui_felicidade(elemento, randint(1,3))
    

def diminuir_energia(elemento):
   Pymagochi.diminui_energia(elemento, randint(1,3))
   

def diminuir_banheiro(elemento):
    Pymagochi.diminui_banheiro(elemento,randint(1,3))


