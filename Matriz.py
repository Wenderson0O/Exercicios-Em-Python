matriz = [[], [], []] #MATRIZ 3x3
for l in range(3):
    for c in range(3):
        matriz[l].append(int(input('NÚMERO: ')))
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='') #:^5 centralizar
    print()
