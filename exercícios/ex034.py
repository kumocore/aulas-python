#Escreva um progama que pergunte o salário do funcionario e calcule o valor do seu aumento.
    #Para salários superiores a R$1.250.00, calcule um aumento de 10%.
    #Para os inferiores ou iguais, o aumento é de 15%.

from time import sleep
print('Digite seu salário abaixo para calcularmos seu aumento!!')
salario = float(input('\nQual é seu salário? R$'))
print('\nCalculando...')
sleep(2)
if salario <= 1200:
  novo = salario + (salario * 15/100)
  print('\nSeu salário de R${:.3f} agora passa a ser de R${:.3f}!'.format(salario, novo))
else:
  novo = salario + (salario * 10/100)
  print('\nSeu salário de R${:.3f} agora passa a ser de R${:.3f}!'.format(salario, novo))
