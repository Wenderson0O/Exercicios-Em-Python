registro = []
for n in range(0, 5):
    num = int(input('Número: '))
    if n == 0 or num > max(registro):
        registro.append(num)
        print('valores registrados no final da linha')
    else:
        for p, c in enumerate(registro):
            if num <= c:
                registro.insert(p, num)
                print(f'valor agregado na posição {p} da linha da linha')
                break
print(registro)
