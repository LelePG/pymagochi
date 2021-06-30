from tkinter import Label

def criar_label(titulo_label, linha, coluna):
    return Label(frame1, text=titulo_label).grid(row = linha, column = coluna)

def criar_label_status(texto_label, linha, coluna):
    return Label(frame1, text=texto_label).grid(row = linha, column = coluna)

def criar_btn(texto_btn, funcao, argumento, linha, coluna):
    return Button(frame1,text = texto_btn, command = lambda: funcao(pymagochi, argumento)).grid(row = linha, column = coluna)