#faça um progama que leia uma frase pelo teclado e mostre
    #quantas vezes aparece a letre "A"
    #em que posição ela aparece a primeira vez
    #em que posição ela aparece a ultima vez
frase = str(input('Digite uma frase: ')).lower().strip()
print('\nSua frase tem um total de {} letras "A"!!'.format(frase.count('a')))
print('A posição que aparece a letra "A" pela primeira vez é: {}'.format(frase.find('a')+1))
print('A posição que aparece a letra "A" pela ultima vez é: {}'.format(frase.rfind('a')+1))
