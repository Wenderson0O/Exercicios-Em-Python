from random import randint

num = list()
def sorteio(lst):
    print('SORTEIO DOS 5 VALORES DA LISTA:', end='')
    for i in range(5):
        nu = randint(1, 10)
        lst.append(nu)
    print()
par = list()
def somapar(lis):
    soma = 0
    for valor in num:
        if valor % 2 == 0:
            par.append(num)
            soma += valor
    print(f'SOMANDO OS VALORES PARES DA LISTA {num}. temos {soma}')


sorteio(num)
print(num)
somapar(par)
