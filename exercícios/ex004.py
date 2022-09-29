#Faça um progama que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas informações possiveis

n = input('Digite algo: ')
print('{} É uma letra?'.format(n), n.isalpha())
print('{} É um numero?'.format(n), n.isnumeric())
print('{} É um alfanumerico?'.format(n), n.isalnum())
print('{} Está todo em letras maiusculas?'.format(n), n.isupper())
print('{} Está todo em letras minusculas?'.format(n), n.islower())
print('{} Pode ser impresso?'.format(n), n.isprintable())
print('{} Contém espaços?'.format(n), n.isspace())
