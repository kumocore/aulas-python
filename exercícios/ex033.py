#Faça um progama que leia três números e mostre qual é o MAIOR e qual é o MENOR

from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('\nAnalisando...')
sleep(3)
maior = n1
if n2 > maior:
  maior = n2
if n3 > maior:
  maior = n3
print('\nO maior número é: {}'.format(maior))
menor = n1
if n2 < menor:
  menor = n2
if n3 < menor:
  menor = n3
print('O menor número é: {}'.format(menor))
