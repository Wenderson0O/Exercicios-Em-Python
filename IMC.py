peso = float(input('Digite o seu peso kg: '))
altura = float(input('Digite a sua altura:  '))
imc = peso / (altura ** 2)  #peso / (altura * altura)
print(f'Seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Abaixo do Peso')
if imc >= 18.5 and peso <= 25:
    print('Peso Ideal')
if imc > 25 and imc <= 35:
    print('Sobrepeso')
if imc > 30 and imc <= 40:
    print('Obesidade')
if imc > 40:
    print('Obesidade mórbida')
