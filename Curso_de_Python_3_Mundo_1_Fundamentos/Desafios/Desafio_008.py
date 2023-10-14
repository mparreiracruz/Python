'''
Desafio 008

Escreva um programa que leia um valor
em metros e o exiba convertido em centímetros
e milímetros.
'''

m = int(input('Digite um valor em metros: '))
centimetros = m * 100
milimetros = m * 1000
print('{} metros em centímetros: {} cm'.format(m, centimetros))
print('{} metros em milímetros: {} mm'. format(m, milimetros))

