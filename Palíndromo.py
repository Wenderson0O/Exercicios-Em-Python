#PALÍNDROMO É UMA FRASE QUE É LIDA DE TRAZ PARA FRENTE
frase = str(input('Digite um frase: ')).upper().strip()
inverso = ''.join(frase) #junta a frase
inverso1 = inverso[::-1] #inverter a frase
if frase == ''.join(reversed(frase)): #reversed para inverte a frase
    print(inverso1) #mostra a frase
    print('É um POLÍNDROMO')
else:
    print(inverso1) #mostra a frase
    print('NÃO é um POLÍNDROMO')
