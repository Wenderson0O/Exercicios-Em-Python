print('Analisador de Triângulos')
reta1 = float(input('Digite o primeiro segmento: '))
reta2 = float(input('Digite o segundo segmento: '))
reta3 = float(input('Digite o terceiro segmento: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima PODEM FORMA triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMA triângulo')
