lista = list()
for i in range(1, 6):
    lista.append(int(input(f'NÚMERO {i}º: ')))

print(f'VOCÊ DIGITOU OS VALORES {lista}')
print(f'MAIOR {max(lista)},NA POSIÇÃO ', end='')
for x, y in enumerate(lista): #SABER QUAIS POSIÇÕES OS NUMEROS DIGITADOS ESTÃO, MESMO NÚMERO REPETIDO
    if y == max(lista):
        print(f'{x+1}...', end=' ')
print() #SERVE PARA PULAR DE LINHA
print(f'MENOR {min(lista)},NA POSIÇÃO ', end='')
for i, r in enumerate(lista):
    if r == min(lista):
        print(f'{i+1}...', end='')
print()
