from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
print('O ângulo de {:.0f} tem o Seno de {:.2f}!'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {:.0f} tem o Cosseno de {:.2f}!'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {:.0f} tem a Tangente de {:.2f}!'.format(angulo, tangente))
