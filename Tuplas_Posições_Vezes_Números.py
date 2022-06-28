numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'O NÚMERO 9 APARECEU {numeros.count(9)} VEZES')
if 3 in numeros:
    print(f'O NÚMERO 3 ESTÁ NA POSIÇÃO {numeros.index((3)) + 1}ª')
else:
    print('O valor 3 NÃO foi digitado em nenhuma posição')
print('OS VALORES PARES DIGITADOS FORAM ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
