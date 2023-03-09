import PySimpleGUI as sg
def texto(texto,tamanho = '_ 12'):
    return sg.Text(texto,font=tamanho, justification='c', expand_x=True)

def br(l = 1):
    return l*"\n"

def a_Space(s = 1):
    return s*" "


import string
def alphabet():
  return list(string.ascii_lowercase)

#print(alphabet())

def my_words():
    my_words = ['abacaxi','bola', 'cachorro', 'dado', 'elefante', 'foca', 'gato' , 'hipopótamo', 'igreja', 'janela', 'kiwi', 'leão', 'macaco', 'nariz', 'ovo', 'pato', 'queijo',
                'rato', 'sapato', 'tatu', 'uva', 'vaca', 'waffer', 'xilito', 'youtube', 'zebra'
                ]
    return my_words
