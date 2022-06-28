pessoas = [[], []]
quant = 0
while True:
    pessoas[0].append(str(input('NOME: ')).strip().title())
    quant += 1
    pessoas[1].append(float(input('PESO: ')))
    while True:
        perg = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()[0]
        if perg in 'SN':
            break
    if perg in 'N':
        break
print('~'*40)
print(f'QUANTIDADE DE PESSOAS CADASTRADAS: {quant}')
print(f'AS PESSOAS MAIS PESADA È:', end=' ')
for q, p in enumerate(pessoas[1]):
    if p == max(pessoas[1]):
        print(f'{pessoas[0][q]}', end='...')
print()
print(f'AS PESSOAS MAIS LEVE È:', end=' ')
for q, p in enumerate(pessoas[1]):
    if p == min(pessoas[1]):
        print(f'{pessoas[0][q]}', end='...')
