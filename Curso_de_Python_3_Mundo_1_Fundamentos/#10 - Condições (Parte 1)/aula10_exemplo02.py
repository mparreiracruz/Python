n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

print('Sua média escolar é {}'.format(m))

if m >= 6.0:
    print('PARABÉNS! Voce foi aprovado!')
else:
    print('Voce foi REPROVADO! Estude mais!')