from random import randint
from Pymagochi import Pymagochi

## Funções de Event Handler (ativadas com o botão)
def aumentar_comida(elemento):
    """Função para aumentar o atribudo comida do objeto elemento passado como 
    parâmetro (espera-se que esse elemento seja uma instância da classe Pymagochi)."""
    Pymagochi.aumenta_comida(elemento,randint(1,5))

def aumentar_bebida(elemento):
    """Função para aumentar o atribudo bebida do objeto elemento passado como 
    parâmetro (espera-se que esse elemento seja uma instância da classe Pymagochi)."""
    Pymagochi.aumenta_bebida(elemento, randint(2,8))
    

def aumentar_felicidade(elemento):
    """Função para aumentar o atribudo feliciade do objeto elemento passado como 
    parâmetro (espera-se que esse elemento seja uma instância da classe Pymagochi)."""
    Pymagochi.aumenta_felicidade(elemento, randint(1,8))
    

def aumentar_energia(elemento):
    """Função para aumentar o atribudo energia do objeto elemento passado como 
    parâmetro (espera-se que esse elemento seja uma instância da classe Pymagochi)."""
    Pymagochi.aumenta_energia(elemento, randint(1,5))
   

def aumentar_banheiro(elemento):
    """Função para aumentar o atribudo banheiro do objeto elemento passado como 
    parâmetro (espera-se que esse elemento seja uma instância da classe Pymagochi)."""
    Pymagochi.aumenta_banheiro(elemento, randint(8,10))
    

## Funções de decremento dos valores padrão que serão instanciadas em threads
def diminuir_comida(elemento):
    """Função para diminuir o atribudo comida do objeto elemento passado como 
    parâmetro (espera-se que esse elemento seja uma instância da classe Pymagochi)."""
    Pymagochi.diminui_comida(elemento, randint(1,3))
    

def diminuir_bebida(elemento):
    """Função para diminuir o atribudo bebida do objeto elemento passado como 
    parâmetro (espera-se que esse elemento seja uma instância da classe Pymagochi)."""
    Pymagochi.diminui_bebida(elemento, randint(1,3))
    

def diminuir_felicidade(elemento):
    """Função para diminuir o atribudo felicidade do objeto elemento passado como 
    parâmetro (espera-se que esse elemento seja uma instância da classe Pymagochi)."""
    Pymagochi.diminui_felicidade(elemento, randint(1,3))
    

def diminuir_energia(elemento):
    """Função para diminuir o atribudo energia do objeto elemento passado como 
    parâmetro (espera-se que esse elemento seja uma instância da classe Pymagochi)."""
    Pymagochi.diminui_energia(elemento, randint(1,3))
   

def diminuir_banheiro(elemento):
    """Função para diminuir o atribudo banheiro do objeto elemento passado como 
    parâmetro (espera-se que esse elemento seja uma instância da classe Pymagochi)."""
    Pymagochi.diminui_banheiro(elemento,randint(1,3))


