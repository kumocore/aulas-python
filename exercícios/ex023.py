#faça um progama que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
    #ex: digite um numero:1834
    #unidade: 4 dezena:3 centena: 8 milhar: 

num = int(input('Digite 4 numeros: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\nUnidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
