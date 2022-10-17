#Desenvolva um progama que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from time import sleep
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print('\nCalculando...')
sleep(2)
if a < b + c and b < a + c and c < a + b:
  print('\nOs segmentos PODEM FORMAR um triângulo!'.format(a, b, c))
else:
  print('\nOs segmentos NÃO PODEM FORMAR um triângulo!'.format(a, b, c))
