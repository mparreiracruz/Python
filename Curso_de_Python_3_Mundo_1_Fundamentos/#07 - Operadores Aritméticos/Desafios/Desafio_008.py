'''
Desafio 008

Escreva um programa que leia um valor
em metros e o exiba convertido em centímetros,
milímetros, quilômetros, equitômetros e decímetros.
'''


m = float(input('Digite um valor em metros: '))

centimetros = m * 100
milimetros = m * 1000
quilometros = m / 1000
equitometros = m / (10**18)
decimetros = m * 10

print('{:.2f} metros em centímetros: {:.2f} cm'.format(m, centimetros))
print('{:.2f} metros em milímetros: {:.2f} mm'. format(m, milimetros))
print('{:.2f} metros em quilômetros: {:.2f} km'.format(m, quilometros))
print('{:.2f} metros em equitômetros: {:.2f} qm'.format(m, equitometros))
print('{:.2f} metros em decímetros: {:.2f} dm'.format(m, decimetros))


'''
m = float(input("Digite um valor em metros: "))

print('{:.2f} metro é igual à {:.2f}cm'.format(m, (m*100)),
      '\n{:.2f} metros é igual à {:.2f}mm'.format(m, (m*1000)), '\n{:.2f} metro é igual à {:.2f}km'
      .format(m, (m/1000)), '\n{:.2f} metros é igual a {:.2f}qm'.format(m, (m / ((10**18)))), '\n{:.2f} metros é igual a {:.2f}dm'
      .format(m, (m*10)))
'''