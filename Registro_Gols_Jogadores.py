time = list()
jogador = dict()
partidas = list()
while True: #entrada de dados
    jogador.clear() #LIMPAR A "LISTA" PARA PODER PEGA O NUMEROS DOS PROXIMOS JOGADORES
    jogador['nome'] = str(input('NOME DO JOGADOR: ')).title().strip()
    quant_part = int(input(f'QUANTAS PARTIDAS {jogador["nome"]} JOGOU? '))
    partidas.clear() #LIMPAR A PARTIDA PARA PODER SOMA OS GOLS, INDIVIDUALMENTE
    for q in range(quant_part):
        partidas.append(int(input(f'QUANTOS GOLS NA PARTIDA {q+1}º ? ')))
    jogador['gols'] = partidas[:] #copia para não aver junção com os gols de outro jogador
    jogador['total'] = sum(partidas) #somar os GOLS
    time.append(jogador.copy()) #copio a lista, registrando os dados
    while True:
        perg = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if perg in 'SN':
            break
        print('ERRO, APENAS VALORES S ou N')
    if perg in 'N':
        break
print('-'*40)
print('code', end='') #saida de dados
for i in jogador.keys(): #cabeçalho
    print(f'{i:<15}', end='')
print() #quebra de linha
print('-'*40)
for k, v in enumerate(time): #mostra quantos gols cada jogador fez e o total em ordem
    print(f'{k:>3} ', end='') #pega a lista, chaves
    for d in v.values(): #pega os valores, nome, gols, total
        print(f'{str(d):<15}', end='')
    print() #quebra de linha
print('-'*40)
while True: #mostra em quais jogos o jogador fez os gols
    bus = int(input('MOSTRA DADOS DE QUAL JOGADOR? [999 para parar]  '))
    if bus == 999:
        break
    if bus >= len(time):
        print(f'ERRO! NÃO EXISTE JOGADOR COM O CÓDIGO {bus}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[bus]["nome"]}: ')
        for i, g in enumerate(time[bus]["gols"]): #dados do jogador
            print(f'NO JOGO {i+1} fez {g} GOLS.')
    print('-'*30)
print('<<VOLTE SEMPRE>>')
