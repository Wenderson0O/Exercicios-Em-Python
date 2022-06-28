n = int(input('Digite um número: '))
tot = 0  #TIVE BASTANTE DIFICULDADE COM ESSE EXERCICIO, PRATICE E ESTUQUE MUITO ESSA PARTE
for c in range(1, n + 1):
    print(c, end='')
    if n % c == 0:
        print(': Número DIVISIVEL.')
        tot += 1
    else:
        print(': NÃO DIVISIVEL.')
print(f'O NÚMERO {n} foi divisível {tot} vezes.')
if tot == 2:
    print('NÚMERO PRIMO!')
else:
    print('Número NÃO PRIMO')
