#A BIBLIOTECA MATH, USADA PARA CALCULAR, UMAS DELAS.
import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print(f'O ângulo de {an} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(an))
print(f'O ângulo de {an} tem o Cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(an))
print(f'O ângulo de {an} tem o Tangente de {tangente:.2f}')
