from random import randint
from time import sleep
jogo = dict()
for i in range(0, 4):
    jogo[i] = randint(1, 6)
    print(f'JOGADOR {i+1} tirou: {jogo[i]}')
    sleep(1)
print('-='*30)
print('RANKING DOS JOGADORES:')
c = 0
for item in sorted(jogo, key=jogo.get, reverse=True):
    c += 1
    print(f'{c}º lugar: jogador {item+1} com,', jogo[item])
    sleep(1)
