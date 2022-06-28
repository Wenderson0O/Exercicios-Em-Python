soma = 0
cont = 0
for i in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'O Senhor informou {cont} PARES, e a soma foi: {soma}')
