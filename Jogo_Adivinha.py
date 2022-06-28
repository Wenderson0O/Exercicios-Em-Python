from random import randint
from time import sleep
sorteio = randint(0, 5) #faz o computador 'pensar'
print('ADIVINHE UM NÚMERO!')
n = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
if n <=5:
    if n == sorteio:
        print('VENCEU, PARABÉNS!')
        print(f'O número escolhido foi {sorteio}')
    else:
        print('PERDEU!')
        print(f'O número escolhido foi {sorteio}')
else:
    print('Número Invalido!')
