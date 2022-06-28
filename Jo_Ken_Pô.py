from random import randint
from time import sleep
computador = randint(0, 2)
print('////Regra do jogo/////')
print('''
0 = PEDRA
1 = TESOURA
2 = PAPEL''')
player = int(input('Digite um número: '))
if player <=2:
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(0.5)
    if player == 0 and computador == 0 or player == 1 and computador == 1 or player == 2 and computador == 2:
        print('empate')
    elif player == 0 and computador == 1:
        print('VOCÊ VENCEU!')
    elif player == 0 and computador == 2:
        print('VOCÊ PERDEU!')
    elif player == 1 and computador == 0:
        print('VOCÊ PERDEU!')
    elif player == 1 and computador == 2:
        print('VOCÊ VENCEU!')
    elif player == 2 and computador == 0:
        print('VOCÊ VENCEU!')
    elif player == 2 and computador == 1:
        print('VOCÊ PERDEU!')
else:
    print('OPÇÃO INVALIDA!')

