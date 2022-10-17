#Faça um progama que leia um ano qualquer e mostre se ele é BISSEXTO 

from datetime import date
from time import sleep 
ano = int(input('Digite um ano, coloque 0 para analisar o ano atual: '))
print('\nANALISANDO...')
sleep(2)
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('O ano de {} é BISSEXTO!'.format(ano))
else:
  print('O ano de {} NÃO é BISSEXTO'.format(ano))
