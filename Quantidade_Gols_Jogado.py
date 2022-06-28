jogador = {}
total = []
gols = 0
jogador['NOME'] = str(input('NOME DO JOGADOR: ')).title()
jogador['QUANT_PART'] = int(input('QUANTAS PARTIDAS JOGADAS: '))
for i in range(jogador['QUANT_PART']):
    jg = int(input(f'JOGO {i+1}, QUANTOS GOLS: '))
    total.append(jg)
    jogador['GOLS'] = total
    gols += jg
    jogador['GOLS_TOTAL'] = gols
print('-='*40)
print(jogador)
print('-='*40)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('='*40)
print(f'O JOGADOR {jogador["NOME"]} jogou {jogador["QUANT_PART"]} partidas.')
for q, g in enumerate(jogador['GOLS']):
    print(f'PARTIDA {q+1}, FEZ {g} GOLS')
print('-'*30)
print(f'TOTAL DE {jogador["GOLS_TOTAL"]} GOLS')
print('-'*30)
