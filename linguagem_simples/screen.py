import PySimpleGUI as sg
def texto(texto,tamanho = '_ 12'):
    return sg.Text(texto,font=tamanho, justification='c', expand_x=True)
#sg.list_of_look_and_feel_values()
#sg.preview_all_look_and_feel_themes()
sg.theme('Blue')
layout = [
    [sg.Text(' ')],
    [texto("Pergunta 01",'_ 20')],
    [sg.Text('')],
    [texto("Para tornar a linguagem mais acessível podemos substituir",)],
    [texto("alguns termos por palavras mais simples ",)],
    [texto("Na frase: 'Iremos pedir a majoração da sua pensão'",)],
    [texto("podemos substituir a palavra - MAJORAÇÂO - por qual outra palavra?")],
    [sg.Text("")],
    [sg.Button("A", key="a"),sg.Text("AUTORIZAÇÃO")],
    [sg.Button("B", key="b"),sg.Text("REDUÇÃO")],
    [sg.Button("C", key="c"),sg.Text("EXCLUSÃO")],
    [sg.Button("D", key="d"),sg.Text("AUMENTO")],
]

layout2 = [
     [sg.Text(' ')],
    [texto("Pergunta 02",'_ 20')],
    [sg.Text('')],
    [texto("Para tornar a linguagem mais acessível podemos substituir",)],
    [texto("alguns termos por palavras mais simples ",)],
    [texto("No termo: 'Declaração de Hipossuficiencia'",)],
    [texto("podemos substituir a palavra - HIPOSSUFICIENCIA - por qual outra palavra?")],
    [sg.Text("")],
    [sg.Button("A", key="a"),sg.Text("BAIXA RENDA")],
    [sg.Button("B", key="b"),sg.Text("CLASSE MÉDIA")],
    [sg.Button("C", key="c"),sg.Text("CLASSE ALTA")],
    [sg.Button("D", key="d"),sg.Text("DOENTE COM PRESSÃO ALTA")],
]

janela = sg.Window("Linguagem Simples", layout)
janela2 = sg.Window("Linguagem Simples", layout2)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "nao vai":
        break

    if evento == "d":
        sg.popup('A Resposta correta é a \nletra <D - AUMENTO >\nAnote sua Resposta',font = '_ 20')
        sg.popup('Parabéns, MAJORAÇÃO é o mesmo que AUMENTO\n vamos para a próxima pergunta',font = '_ 20')
        janela.close()
    else:
        sg.popup('você errou, tente novamente',font = '_ 20')
        continue
    while evento != "a":
        evento, valores = janela2.read()
        if evento != "a":
            sg.popup('você errou, tente novamente',font = '_ 20')
            continue
    sg.popup('A Resposta correta é a \nletra <A - BAIXA RENDA>\nAnote sua Resposta',font = '_ 20')
    sg.popup('Parabéns, HIPOSSUFICIENCIA é o mesmo que BAIXA RENDA\npegue as respostas no envelope \ne vá ao ponto de encontro', font = '_ 20')
            
        

janela.close()