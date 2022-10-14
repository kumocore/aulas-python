#crie um progama que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = str(input('Digite seu nome completo: ')).strip()
print('A informação de que você tem "Silva" no nome é {}!!'.format('SILVA' in nome.upper()))
