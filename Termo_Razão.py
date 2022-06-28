primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 10
while c > 0:
    print(primeiro_termo, end=' ')
    primeiro_termo += razao
    c -= 1
