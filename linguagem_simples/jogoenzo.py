import PySimpleGUI as sg
from txtformat import texto, alphabet, my_words

sg.theme('DarkBrown4')
layout = [
    [sg.Text(' ')],
    [texto("JOGO DO ENZO",'_ 20')],
    [sg.Text('')],
    
    [sg.Text("")],
    [sg.Button("A", key="a", size = (5,2)),sg.Button("B", key="b", size = (5,2)),sg.Button("C", key="c", size = (5,2)),sg.Button("D", key="d", size = (5,2)),sg.Button("E", key="e", size = (5,2))],
    [sg.Button("F", key="f", size = (5,2)),sg.Button("G", key="g", size = (5,2)),sg.Button("H", key="h", size = (5,2)),sg.Button("I", key="i", size = (5,2)),sg.Button("J", key="j", size = (5,2))],
    [sg.Button("K", key="k", size = (5,2)),sg.Button("L", key="l", size = (5,2)),sg.Button("M", key="m", size = (5,2)),sg.Button("N", key="n", size = (5,2)),sg.Button("O", key="o", size = (5,2))],
    [sg.Button("P", key="p", size = (5,2)),sg.Button("Q", key="q", size = (5,2)),sg.Button("R", key="r", size = (5,2)),sg.Button("S", key="s", size = (5,2)),sg.Button("T", key="t", size = (5,2))],
    [sg.Button("U", key="u", size = (5,2)),sg.Button("V", key="v", size = (5,2)),sg.Button("W", key="w", size = (5,2)),sg.Button("X", key="x", size = (5,2)),sg.Button("Y", key="y", size = (5,2))],
    [sg.Button("", key="", size = (5,2)),sg.Button("", key="", size = (5,2)),sg.Button("Z", key="z", size = (5,2)),sg.Button("", key="", size = (5,2)),sg.Button("", key="", size = (5,2))],
]

def show_window(letra, palavra):
    janela = sg.Window("Jogo do Enzo", layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "nao vai":
            break
        if evento in letra:
            for i in range(len(letra)):
                if letra[i] == evento:
                    sg.popup(f'{letra[i].upper()} de {palavra[i].upper()}',title = ":) PARABÉNS!!!", font = '_ 20', modal = True)
                escolha = palavra[i]
                if escolha[0] == evento:
                    for i in range(len(escolha)):
                        sg.popup(f'    {escolha[i].upper()}',title = ":) PARABÉNS!!!", font = '_ 20', modal = True)
    
    janela.close()

alfabeto = alphabet()
palavras = my_words()
show_window(alfabeto, palavras)
