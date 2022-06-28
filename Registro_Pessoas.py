registro = dict()
regis_inter = list()
soma = 0
while True: #entrada de dados
    registro.clear() #LIMPAR PARA PODER REGISTAR A PROXIMA PESSOA
    registro['NOME'] = str(input('NOME: ')).title()
    while True:
        registro['SEXO'] = str(input('SEXO [F/M]: ')).upper().strip()[0]
        if registro['SEXO'] in 'MF':
            break
        print('ERRO, APENAS M ou F.')
    registro['IDADE'] = int(input('IDADE: '))
    soma += registro['IDADE'] #soma
    regis_inter.append(registro.copy())
    while True:
        resp = str(input('DESEJA SAIR? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO, TENTE NOVAMENTE!')
    if resp == 'S':
        break
#SAIDA DE DADOS
divisao = soma / len(regis_inter)
print(regis_inter)
print(f'QUATIDADE DE PESSOAS REGISTRADAS: {len(regis_inter)}')
print(f'A MÉDIA DE IDADE DO GRUPO: {divisao:5.2f} anos')
print('-'*30)
print('MULHERES REGISTRADAS:', end='')
for p in regis_inter: #PEGA OS NOMES DE TODAS AS MULHERES.
    if p['SEXO'] in 'F':
        print(f' {p["NOME"]}, ', end='')
print()
print('-'*30)
print('AS PESSOAS ACIMA DA MÉDIA:', end='')
for a in regis_inter: #PEGA A LISTA DE PESSOAS ACIMA DA MÉDIA.
    if a['IDADE'] > divisao:
        print('     ')
        for k, v in a.items():
            print(f' {k}: {v}.', end='')
        print()
