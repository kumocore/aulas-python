larg = float(input('Altura da parede: '))
alt = float(input('Comprimento da parede: '))
área = larg * alt
print('\nSua parede tem a dimensão de {}x{} e sua area é de {}m²!'.format(larg, alt, área))
tinta = área / 2
print('A quantidade necessaria de tinta para pintar a parede é de {}L!'.format(tinta))
