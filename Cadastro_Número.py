cadastro = list()
while True:
    num = int(input('NÚMERO: '))
    if num not in cadastro: #CASO O NÚMERO SEJA REPETIDO, ELE N ACEITA
        cadastro.append(num)
        print('VALOR ADICIONADO COM SUCESSO')
    else:
        print('VALOR REPETIDO, NÃO ADICIONADO!')

    while True:
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if opcao in 'SN': #LOOP DA PERGUNTA
            break #PARA A PERGUNTA, ENQUANTO FOR DIGITADA S/N

    if opcao in 'N': #SE OPÇÂO FOR N ELE PARA O LOOP
        break
cadastro.sort()
print(f'CADASTRO EM ORDEM CRESCENTE {cadastro}')
