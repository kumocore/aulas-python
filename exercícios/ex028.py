#Escreva um progama que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
    #O progama deverá escrever na tela se o usuario perdeu ou venceu.

from random import randint
from time import sleep
numero = randint(0, 5)
print('-' * 35)
print(' Um número de 0 à 5 foi escolhido')
print('-' * 35)
adivinhe = int(input('\nTente advinhar o número: '))
print('\nPROCESSANDO...')
sleep(3)
if adivinhe == numero:
  print('\nParábens, você acertou! :)')
else:
  print('\nVocê errou! :(')
print('\nO número escolhido foi o número {}!'.format(numero))
