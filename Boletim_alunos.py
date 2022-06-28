boletim = list()
while True:
    nome = str(input('NOME: ')).strip().title()
    nota1 = float(input('NOTA 1º: '))
    nota2 = float(input('NOTA 2º: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    resp = str(input('DESEJA CONTINUAR? [S/N] ')).upper()[0]
    if resp in 'N':
        break
print('='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('='*30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('='*30)
    opcs = int(input('MOSTRA NOTAS DE QUAL ALUNO? [999 interromper]: '))
    print('='*30)
    if opcs == 999:
        print('FINALIZADO')
        print('='*30)
        break
    if opcs <= len(boletim) - 1:
        print(f'NOTAS DE {boletim[opcs][0]} SÃO {boletim[opcs][1]}')
print('VOLTE SEMPRE')
