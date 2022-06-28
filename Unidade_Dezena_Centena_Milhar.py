while True:
    n = int(input('Digite o número ate 9999 [0 para Sair]: '))
    u = n // 1 % 10
    d = n // 10 % 10
    c = n // 100 % 10
    m = n // 1000 % 10
    print(f'Unidade {u}')
    print(f'Dezena {d}')
    print(f'Centena {c}')
    print(f'Milhar {m}')
    if n == 0:
        break
