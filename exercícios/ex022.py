#crie um progama que leia o nome completo de uma pessoa e mostre:
  #o nome com todas as letras maiusculas
  #o nome com todas letras minusculas
  #quantas letras ao todo (sem considerar espaços)
  #quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome me minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format((len(nome) - nome.count(' '))))
lista = nome.split()
print('Seu primeiro é {} e ele tem {} letras'.format(lista[0], len(lista[0])))
