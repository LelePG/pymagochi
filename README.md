# Pymagochi - um tamagochi, em Python

<img src="imagens/PymagochiTotal.png" width = 400>

## O que é este projeto?
Este projeto se trata de uma interface gráfica criada em python com a biblioteca **tkinter** que simula o comportamento de um Tamagochi, onde você precisa cuidar do Pymagochi, alimentando-o, dando água para ele, fazendo com que ele durma, etc.  

## Como utilizar esse projeto?
Para brincar com o Pymagochi, basta fazer o donwload do repositório digitando `git clone https://github.com/LelePG/pymagochi.git` no terminal, ou fazendo o download do arquivo .zip clicando no botão verde `code`.

Para rodar o programa, basta rodar o comando `python3 main.py` dentro da pasta onde este arquivo se encontra. Isso abrirá a interface gráfica que mostra o Pymagochi, seus status e botões para que você interaja com os status aumentando-os quando eles estiverem muito baixos.

Caso o status de banheiro chegue a 0, uma mensagem é mostrada na tela pedindo que você limpe a caixa de areia do Pymagochi, e se algum dos outros estados chegar a 0, o Pymagochi morre, e você deve reinciar o jogo. Avisos sonoros estão configurados para estas duas situações.

## Módulos utilizados
Foi criado um pacote chamado **manipulador_interface** para centralizar algumas das funções utilizadas na implementação (que se encontram documentadas), e além disso o projeto do Pymagochi conta com as seguintes importações:
- tkinter 
- tkinter.messagebox
- random.randint
- threading
- audioplayer
- os

## Como este projeto funciona?
O Pymagochi trabalha com múltiplas threads, sendo uma delas responsável por atualizar a interface e outra responsável por fazer o decremento dos status do Pymagochi. Quando a tela é fechada ou algum dos estados significativos do objeto Pymagochi instanciado atinge 0, o jogo é encerrado.

Existem também algumas constantes definidas no início do arquivo main.py que podem ser utilizadas para personalizar algumas características do jogo. 

## Recursos
O projeto do Pymagochi utiliza imagens e audios, que se encontram nas pastas *imagens* e *audio*. Na pasta imagens, além das imagens utilizadas na implementação do projeto, existe também uma imagem com mais alguns desenhos, de onde saiu o desenho do Pymagochi.

## Links úteis
Alguns links que utilizei na criação do projeto:
- [Como instalar o tkinter](https://stackoverflow.com/questions/4783810/install-tkinter-for-python)
- [Referencia do audioplayer](https://pypi.org/project/audioplayer/)
- [How to use Tkinter label](https://pythonguides.com/python-tkinter-label/)
- [How to use images as background in tkinter](https://www.geeksforgeeks.org/how-to-use-images-as-backgrounds-in-tkinter/)
