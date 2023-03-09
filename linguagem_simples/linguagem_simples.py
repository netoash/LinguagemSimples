import time
import os

def contagem_Regressiva(tempo = 10):
    for i in range(tempo,0,-1):
        time.sleep(1)
        print(f"{br(2)}{a_Space(70)}{i}...")

def clear_Terminal(tempo = 5):
    contagem_Regressiva(tempo)
    os.system('cls') or None

def itens(a,b,c,d,e = 0):
    if e == 1 :
        return print(f"<A>{a}\n<B>{b}\n<C>{c}\n<D>{d}")
    else:
        return print(f"{a_Space(50)}<A>{a}{br(2)}{a_Space(50)}<B>{b}{br(2)}{a_Space(50)}<C>{c}{br(2)}{a_Space(50)}<D>{d}")

def br(l = 1):
    return l*"\n"

def a_Space(s = 1):
    return s*" "
################################################################################################################

space = ["", " ", "  ", "   ", "    ", "     "]
resp_dpge = ["AUMENTO", "AUMENTAR", "D"]
chance = 5

print(f"{br(10)}{a_Space(50)}Para tornar a linguagem mais acessível podemos {br(2)}{a_Space(50)}substituir alguns termos por palavras mais simples{br(2)}{a_Space(50)}Na frase: 'Iremos pedir a majoração da sua pensão' {br(2)}{a_Space(43)}podemos substituir a palavra - MAJORAÇÂO - por qual outra palavra?{br(2)}") 
itens(" AUTORIZAÇÃO", " REDUÇÃO", " EXCLUSÃO"," AUMENTO")

while True:
 resp = input(f"{br(2)}{a_Space(43)}RESPOSTA: ")
 if resp.upper() in resp_dpge:
  print(f"{br(2)}{a_Space(50)}A resposta <{resp.upper()}> está correta, PARABÉNS!!!{br(2)}{a_Space(50)}MAJORAÇÃO é o mesmo que AUMENTO{br(2)}{a_Space(50)}Anote a RESPOSTA{br(2)}{a_Space(50)}Proxima pergunta em: ")
  clear_Terminal()
  break
 elif resp in space:
  print(f"{br(2)}{a_Space(50)}A resposta está em branco, tente novamente") 
 else:
  chance -= 1
  print(f"{br(2)}{a_Space(50)}A resposta <{resp.upper()}> está errada")
  if chance == 0:
    print(f"{br(2)}{a_Space(50)}Você não possui mais tentativas{br(2)}{a_Space(50)}Vamos para a proxima pergunta")
    clear_Terminal(3)
    break
  print(f"{br(2)}{a_Space(50)}Você possui apenas {chance} tentativa(s)")
  continue


space = ["", " ", "  ", "   ", "    ", "     "]
resp_sdhds = ["BAIXA RENDA", "POBRE", "SEM CONDIÇÃO", "A"]
chance = 5

print(f"{br(10)}{a_Space(50)}Para tornar a linguagem mais acessível podemos {br(2)}{a_Space(50)}substituir alguns termos por palavras mais simples{br(2)}{a_Space(50)}No termo: 'Declaração de Hipossuficiencia' {br(2)}{a_Space(43)}podemos substituir a palavra - HIPOSSUFICIENCIA - por qual outra palavra?{br(2)}")
itens(" BAIXA RENDA", " CLASSE MÉDIA", " CLASSE ALTA", " DOENTE COM PRESSÃO ALTA")

while True:
 resp = input(f"{br(2)}{a_Space(43)}RESPOSTA: ")
 if resp.upper() in resp_sdhds:
  print(f"{br(2)}{a_Space(50)}A resposta <{resp.upper()}> está correta, PARABÉNS!!!{br(2)}{a_Space(50)}HIPOSSUFICIENCIA é o mesmo que BAIXA RENDA{br(2)}{a_Space(50)}Anote a RESPOSTA")   
  print(f"{br(2)}{a_Space(50)}A tela ira se fechar em :")
  contagem_Regressiva(10)
  # para cmd do windows usar
  #clear_Terminal(10)
  break
 elif resp in space:
  print(f"{br(2)}{a_Space(50)}A resposta está em branco, tente novamente") 
 else:
  chance -= 1
  print(f"{br(2)}{a_Space(50)}A resposta <{resp.upper()}> está errada")
  if chance == 0:
    print(f"{br(2)}{a_Space(50)}Você não possui mais tentativas{br(2)}{a_Space(50)}Retorne ao ponto de encontro{br(2)}{a_Space(50)}A tela ira se fechar em :")
    contagem_Regressiva(10)
    #para cmd do windows usar
    #clear_Terminal(10)
    break
  print(f"{br(2)}{a_Space(50)}Você possui apenas {chance} tentativa(s)")
  continue


