print("Desenvolvido por: @netoash\nCom colaboração de : @lais.fr")
import PySimpleGUI as sg
def texto(texto,tamanho = '_ 12'):
    return sg.Text(texto,font=tamanho, justification='c', expand_x=True)

def textol(texto,tamanho = '_ 12'):
    return sg.Text(texto,font=tamanho, justification='l', expand_x=True)

def showScreen(layout, opcao, resposta, fim=0):
    janela = sg.Window("Linguagem Simples", layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "nao vai":
            break

        if evento == opcao:
            sg.popup(f'A Resposta correta é a \nletra <{resposta}>\nAnote sua Resposta',title = ":) PARABÉNS!!!", font = '_ 20', modal = True)
            
            if fim == 0:
                sg.popup('PARABÉNS!!!\n vamos para a próxima pergunta',title = ":) PARABÉNS!!!",font = '_ 20', modal = True)
            
                break
            else:
                sg.popup('PARABÉNS!!!\npegue as letras correspondentes de \ncada respostas no envelope \ne vá ao ponto de encontro',title = ":) PARABÉNS!!!", font = '_ 20', modal = True)
                break
        else:
            sg.popup('você errou, tente novamente',title = ":( que pena!!!", font = '_ 20', modal = True)
            continue

    janela.close()


#sg.list_of_look_and_feel_values()
#sg.preview_all_look_and_feel_themes()
sg.theme('DarkPurple1')
pergunta1 = [
    [sg.Text(' ')],
    [sg.Image(sg.EMOJI_BASE64_HAPPY_HEARTS ),texto("Pergunta 01",'_ 20')],
    [sg.Text(''), ],
    [texto("Escolha",)],
    [texto("qual das opções abaixo",)],
    [texto("NÃO é",)],
    [texto("um benefício da linguagem simples.")],
    [sg.Text("")],
    [sg.Button("A", key="a"),textol("Aproximar o Governo das pessoas")],
    [sg.Button("B", key="b"),textol("Fortalecer o Atendimento Humanizado")],
    [sg.Button("C", key="c"),textol("Inovar de forma simples")],
    [sg.Button("D", key="d"),textol("Poder usar mais gírias")],
    [sg.Text("Desenvolvido por: @netoash", font='Helvetica 7', text_color= 'gray', justification = 'r',expand_x=True)],
]

pergunta2 = [
    [sg.Text(' ')],
    [sg.Image(sg.EMOJI_BASE64_HAPPY_JOY ), texto("Pergunta 02",'_ 20')],
    [sg.Text('')],
    [texto("Escolha as palavra que preenchem a frase:",)],
    [texto("No ano de ________ surge o (011).lab,",)],
    [texto("laboratório de inovação da",)],
    [texto("prefeitura de_______________.")],
    [sg.Text("")],
    [sg.Button("A", key="a"),textol("2017 / São Paulo")],
    [sg.Button("B", key="b"),textol("2020 / Fortaleza")],
    [sg.Button("C", key="c"),textol("2017 / Fortaleza")],
    [sg.Button("D", key="d"),textol("2020 / São Paulo")],
    [sg.Text("Desenvolvido por: @netoash", font='Helvetica 7', text_color= 'gray', justification = 'r',expand_x=True)],
]

pergunta3 = [
    [sg.Text(' ')],
    [sg.Image(sg.EMOJI_BASE64_HAPPY_BIG_SMILE ),texto("Pergunta 03",'_ 20')],
    [sg.Text('')],
    [texto("Jornalista e empreendedora brasileira.",)],
    [texto("Pioneira da Linguagem Simples no Brasil.",)],
    [texto("Referencia no tema da Linguagem Simples.",)],
    [texto("De quem estamos falando?")],
    [sg.Text("")],
    [sg.Button("A", key="a"),textol("Sandra Fischer")],
    [sg.Button("B", key="b"),textol("Jacqueline Fischer")],
    [sg.Button("C", key="c"),textol("Heloísa Fischer")],
    [sg.Button("D", key="d"),textol("Vera Fischer")],
    [sg.Text("Desenvolvido por: @netoash", font='Helvetica 7', text_color= 'gray', justification = 'r',expand_x=True)],
]

pergunta4 = [
    [sg.Text(' ')],
    [sg.Image(sg.EMOJI_BASE64_HAPPY_WINK ), texto("Pergunta 04",'_ 20')],
    [sg.Text('')],
    [texto("Em qual dessas atividades",)],
    [texto("NÃO houve",)],
    [texto("a participação da Comissão da",)],
    [texto("Linguagem Simples")],
    [sg.Text("")],
    [sg.Button("A", key="a"),textol("E-mail de Recuperação de Senha")],
    [sg.Button("B", key="b"),textol("Grupo focal da pesquisa de clima e GPTW")],
    [sg.Button("C", key="c"),textol("Painel de chamada de senhas.")],
    [sg.Button("D", key="d"),textol("Guia de Serviços do Portal meuvaptvupt")],
    [sg.Text("Desenvolvido por: @netoash", font='Helvetica 7', text_color= 'gray', justification = 'r',expand_x=True)],
]

pergunta5 = [
    [sg.Text(' ')],
    [sg.Image(sg.EMOJI_BASE64_FINGERS_CROSSED ), texto("Pergunta 05",'_ 20')],
    [sg.Text('')],
    [texto("1 - Pense no documento e no público-alvo do documento.",)],
    [texto("2 - Aplique os Dez passos e Faça um teste com o público-alvo do documento.",)],
    [texto("3 - Revise o documento a partir das impressõesdo público-alvo.",)],
    [texto("Sobre as etapas para simplificar a linguagem:")],
    [sg.Text("")],
    [sg.Button("A", key="a"),textol("1 e 2 estão corretos")],
    [sg.Button("B", key="b"),textol("2 e 3 estão corretos")],
    [sg.Button("C", key="c"),textol("1 e 3 estão corretos")],
    [sg.Button("D", key="d"),textol("D - Todas as opções estão corretas")],
    [sg.Text("Desenvolvido por: @netoash", font='Helvetica 7', text_color= 'gray', justification = 'r',expand_x=True)],
]


showScreen(pergunta1,"d","D - Poder usar mais gírias")
showScreen(pergunta2,"a","A - 2017 / São Paulo")
showScreen(pergunta3,"c","C - Heloísa Fischer")
showScreen(pergunta4,"b","B - Grupo focal da pesquisa de clima e GPTW")
showScreen(pergunta5,"d","D - Todas as opções estão corretas",1)
