salario = float(input('Quanto é seu salario mensal? R$'))
novo = salario + (salario * 15/100)
print('Seu salario com 15% de aumento fica R${:.2f}!'.format(novo))
