numeros = int(input('Digite o PRIMEIRO número: '))
numeros1 = int(input('Digite o SEGUNDO número: '))
opcao = 1
while opcao != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Digite a sua OPÇÃO: '))
    if opcao >= 1 and opcao <5:
        if opcao == 1:
            soma = numeros + numeros1
            print(f'A soma dos números {numeros} + {numeros1} foram {soma}')
        elif opcao == 2:
            multiplicar = numeros * numeros1
            print(f'A multiplicação dos números {numeros} e {numeros1} foram {multiplicar}')
        elif opcao == 3:
            if numeros > numeros1:
                maior = numeros
                print(f'O maior número é {maior}')
            else:
                maior = numeros1
                print(f'O maior número é {maior}')
        elif opcao == 4:
            numeros = novos_numeros = int(input('Novo primeiro número: '))
            numeros1 = novos_numeros1 = int(input('Novo segundo número: '))

print('OBRIGADO, VOLTE SEMPRE.')
