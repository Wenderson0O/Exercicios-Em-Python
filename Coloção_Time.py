campeonato = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
              'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
              'Atlético-GO', 'Santos', 'Ceará-SC', 'Internacional',
              'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
              'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('='*20)
print(f'OS CINCOS PRIMEIOS COLOCADOS SÃO: {campeonato[0:5]}')
print('='*20)
print(f'OS ULTIMOS 4 COLOCADOS SÃO: {campeonato[16:]}')
print('='*20)
print(f'TIME EM ORDEM ALFABETICA: {sorted(campeonato)}')
print('='*20)
print(f'CHAPECOENSE ESTÁ NA {campeonato.index("Chapecoense")+1}° POSIÇÃO') #POSIÇÃO

