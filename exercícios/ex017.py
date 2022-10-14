from math import hypot
ca = float(input('Digite o Cateto Adjacente: '))
co = float(input('Digite o Cateto Oposto: '))
hi = hypot(ca, co)
print('O comprimento da hipotenusa é {:.2f}!'.format(hi))
