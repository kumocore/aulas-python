dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos km você percorreu com o carro? '))
preço = (dias * 60) + (km * 0.15)
print('\nVocê percorreu {}km \nAlugou o carro por {} dias \nO preço total fica R${}'.format(km, dias, preço))
