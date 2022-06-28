valores = [[], []]
for i in range(0, 7):
    numeros = int(input(f'NÚMERO {i}º: '))
    if numeros % 2:
        valores[0].append(numeros) #IMPA
        #print('IMPA',valores[0])
    else:
        valores[1].append(numeros) #PAR
        #print('PAR',valores[1])
valores[0].sort()
valores[1].sort()
print(f'OS VALORES IMPARES: {valores[0]}')
print(f'OS VALORES PARES: {valores[1]}')
