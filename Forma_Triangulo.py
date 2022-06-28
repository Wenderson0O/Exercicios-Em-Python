reta1 = float(input('Digite o primeiro segmento: '))
reta2 = float(input('Digite o segundo segmento: '))
reta3 = float(input('Digite o terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Pode FORMA UM TRIANGULO', end=' ')
    if reta1 == reta2 == reta3:
        print('Equilátero')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('Isósceles')
    elif reta1 != reta2 != reta3 != reta1: #A é diferente de B e B é diferente de C, mas tbm tera que coloca A é diferente de C
        print('Escaleno')
else:
    print('Não pode forma um Triangulo!')
