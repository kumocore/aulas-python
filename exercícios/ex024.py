#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "SANTO"

cidade = str(input('Em que cidade você nasceu? ')).strip()
print('A informação de que sua cidade tem "Santo" no nome é {}!!'.format(cidade[:5].upper() == 'SANTO'))
