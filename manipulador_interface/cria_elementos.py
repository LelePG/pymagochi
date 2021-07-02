from tkinter import *

## Funções de criação de elementos
def criar_label(frame,titulo_label, linha, coluna):
    l = Label(frame, text=titulo_label, font=("arial", 9), bg = "#764c22", fg="#000")
    l.grid(row = linha, column = coluna)
    return l


def criar_btn(frame,elemento_principal, texto_btn, funcao, linha, coluna):
    return Button(frame,text = texto_btn, command = lambda: funcao(elemento_principal),font=("arial", 9), fg="#000", bg = "#764c22",borderwidth=3, relief="ridge").grid(row = linha, column = coluna)
