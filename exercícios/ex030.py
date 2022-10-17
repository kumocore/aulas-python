#Crie um progama que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.

numero = int(input('Digite um numero qualquer: '))
if numero % 2 == 0:
  print('\nO número {} é PAR!'.format(numero))
else:
  print('\nO número {} é IMPAR!'.format(numero))
