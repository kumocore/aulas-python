preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 5/100)
print('O preço do seu produto com 5% de desconto fica R${:.2f}'.format(novo))
