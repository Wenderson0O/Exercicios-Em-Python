num = 1
total = 0
soma = 0
num = int(input('NÚMERO [999 para parar]: '))
while num != 999: #TRUE
    total += 1 #QUANTIDADE DE VEZES
    soma += num #SOMA
    num = int(input('NÚMERO [999 para parar]: ')) #O FLEG NÃO VAI SER SOMADO, SE O NÚMERO FOR IGUAL A 999, ELE SAI N SOMA
print(f'O TOTAL DE NÚMEROS DIGITADOS FOI {total}') #FALSE
print(f'A SOMA DE TODOS OS NÚMEROS FOI {soma}')
