#Escreva um progama que leia a velocidade de um carro.
    #Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
    #A multa vai custar R$7,00 por cada Km acima do limite
    
velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
  cobrar = (velocidade - 80) * 7
  print('Você ultrapassou o limite de 80Km/h, você foi multado no valor de {:.2f}!'.format(cobrar))
print('Tenha um bom dia, dirija com segurança!')
