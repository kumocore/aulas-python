real = float(input('Quantos reais você tem na sua carteira? R$'))
dolar = real / 5.41
print('Você pode comprar U${:.2f} com R${:.2f}'.format(dolar, real))
