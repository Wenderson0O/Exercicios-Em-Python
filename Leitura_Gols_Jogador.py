def ficha(nome=0, gols=0):
    nome = str(input('NOME DO JOGADOR: ')).title()
    if nome == '':
        nome = '<DESCONHECIDO>'
    gols = str(input(f'QUANTOS GOLS O JOGADOR {nome} FEZ? '))
    if gols == '':
        gols = 0
    print(f'O JOGADOR {nome} FEZ {gols} GOLS NO CAMPEONATO.')


#PROGRAMA PRINCIPAL
ficha(nome=0, gols=0)
