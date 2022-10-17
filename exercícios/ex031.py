#Desenvolva um progama que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

viagem = float(input('Quantos Km tem sua viagem? '))
if viagem <= 200:
  cobrar = viagem * 0.50
else:
  cobrar = viagem * 0.45
print('Sua viagem é de {}Km!\nO valor fica R${:.2f}!'.format(viagem, cobrar))
