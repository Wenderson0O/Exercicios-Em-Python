from random import randint
from time import sleep
jogos = []
palpite = []
print('='*40)
print('             MEGA SENA')
print('='*40)
gerados = int(input('QUANTOS PALPITES SERAM GERADOS? '))

for i in range(gerados):
    for x in range(0, 6):
        jogos.append(randint(1, 60))
    jogos.sort()
    palpite.append(jogos[:])
    jogos.clear()
o = 1
for p in palpite:
    sleep(1)
    print(f'JOGO {o}º:', p)
    o += 1
print('BOA SORTE.')
