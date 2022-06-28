maior_idade = mulheres_menor_20 = homens = 0
opcao = 'S'
while opcao == 'S':
    print('~'*40)
    print('AUTENTICAÇÃO DE IDADE / SEXO')
    print('~'*40)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF': 
        sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
    print('='*40)
    opcao = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()[0]
    if idade >= 18:
        maior_idade += 1
    if sexo == 'F':
        if idade < 20:
            mulheres_menor_20 += 1
    if sexo == 'M':
        homens += 1
print('~'*40)
print(f'''

O TOTAL DE PESSOAS MAIORES DE IDADE SÃO {maior_idade}
A QUANTIDADE DE HOMENS CADASTRADOS É {homens}
QUANTIDADE DE MULHERES QUE TEM MENOS DE 20 ANOS É {mulheres_menor_20}''')
print('~'*40)
