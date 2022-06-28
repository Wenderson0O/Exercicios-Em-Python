#Faça um mini-sistema que utilize o interactive help do python.
#O usuário vai digitar e o manual vai aparecer. Quando o usuário
#digitar a palavra FIM, o programa se encerrará
from time import sleep
def ajuda(com):
    titulo('Acessando o Manual de Comando')
    help(com)
    sleep(2)


def titulo(msg):
    tamanho = len(msg) + 4
    print('=' * tamanho)
    print(f'  {msg}')
    print('=' * tamanho)
    sleep(1)


#programa principal
comando=''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    titulo('Para sair do manual clike Q')
    titulo('SAIR DIGITE FIM')
    comando = str(input('FUNÇÃO OU BIBLIOTECA: '))
    if comando.upper() =='FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO')
