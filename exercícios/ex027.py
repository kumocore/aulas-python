#faça um progama que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome 
#separadamente
    #ex: ana maria de souza
    #primeiro = ana 
    #ultimo = souza
nome = str(input('Digite seu nome completo: '))
n = nome.split()
print('Primeiro nome: {}'.format(n[0]))
print('Ultimo nome: {}'.format(n[-1]))
