import PySimpleGUI as sg
from txtformat import texto, alphabet, my_words
print('\n\n\n                                                             BEM VINDOS AO JOGO DO ENZO!!!')
sg.theme('Topanga')

layout = [
    [texto("JOGO DO ENZO",'_ 20')],
    [sg.Text("")],[sg.Image(r'C:\Users\anton_000\Desktop\linguagem_simples\img\ehch.png' , size = (300,300),expand_x=True)],
    #[sg.Image(sg.EMOJI_BASE64_HAPPY_HEARTS )],
    #[sg.Text('')],
    [sg.Button("A", key="a", size = (7,2)),sg.Button("B", key="b", size = (7,2)),sg.Button("C", key="c", size = (7,2)),sg.Button("D", key="d", size = (7,2)),sg.Button("E", key="e", size = (7,2))],
    [sg.Button("F", key="f", size = (7,2)),sg.Button("G", key="g", size = (7,2)),sg.Button("H", key="h", size = (7,2)),sg.Button("I", key="i", size = (7,2)),sg.Button("J", key="j", size = (7,2))],
    [sg.Button("K", key="k", size = (7,2)),sg.Button("L", key="l", size = (7,2)),sg.Button("M", key="m", size = (7,2)),sg.Button("N", key="n", size = (7,2)),sg.Button("O", key="o", size = (7,2))],
    [sg.Button("P", key="p", size = (7,2)),sg.Button("Q", key="q", size = (7,2)),sg.Button("R", key="r", size = (7,2)),sg.Button("S", key="s", size = (7,2)),sg.Button("T", key="t", size = (7,2))],
    [sg.Button("U", key="u", size = (7,2)),sg.Button("V", key="v", size = (7,2)),sg.Button("W", key="w", size = (7,2)),sg.Button("X", key="x", size = (7,2)),sg.Button("Y", key="y", size = (7,2))],
    [sg.Button("MEU NOME", key="nome", size = (15,2)),sg.Button("Z", key="z", size = (10,2)),sg.Button("SAIR", key="sair", size = (15,2))],
]

def show_window(letra, palavra):
    janela = sg.Window("Jogo do Enzo", layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "sair":
            sg.PopupOK('OBRIGADO POR JOGAR')
            break
        if evento in letra:
            for i in range(len(letra)):
                if letra[i] == evento :
                    sg.popup(f'    Letra   {letra[i].upper()}    \n      \n{palavra[i].upper()}',title = ":) PARABÉNS!!!", font = '_ 20', modal = True)
        if evento == 'nome':
            sg.popup(f'ENZO\nHENRIQUE',title = ":) PARABÉNS!!!", font = '_ 20', modal = True)

    janela.close()

alfabeto = alphabet()
palavras = my_words()
show_window(alfabeto, palavras)
