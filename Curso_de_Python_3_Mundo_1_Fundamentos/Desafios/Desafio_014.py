'''
Desafio 014

Escreva um programa que converta uma
temperatura em celsios para farenheit.
'''

c = float(input('Digite a temperatura em celsius: '))

#f = (c * 9 / 5) + 32
f = 9 * c / 5 + 32

print('{} graus celsius é igual a {:.2f} graus farenheit'.format(c, f))
