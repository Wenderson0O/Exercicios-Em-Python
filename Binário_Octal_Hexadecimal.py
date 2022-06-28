n = int(input('Digite um número: '))
print('''0 = BINÁRIO
1 = OCTAL
2 = HEXADECIMAL''')
opçao = int(input('Digite a opção: '))
if opçao == 0:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opçao == 1:
   print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif opçao == 2:
    print(f'{n} convertido para Hexadecimal é igual a {hex(n)[2:]}')
else:
    print('OPÇÃO INVALIDA!')
