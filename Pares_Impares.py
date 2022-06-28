total_numero = []
pares = []
impares = []
while True:
    num = int(input('Número: '))
    total_numero.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    while True:
        perg = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()[0]
        if perg in 'SN':
            break
    if perg in 'N':
        break
print(f'''
OS NÚMEROS DIGITADOS SÃO {total_numero}
OS NÚMEROS PARES SÃO {pares}
OS NÚMEROS IMPAR SÃO {impares}''')
