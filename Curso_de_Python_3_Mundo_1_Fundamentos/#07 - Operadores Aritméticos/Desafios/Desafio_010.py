'''
Desafio 010

Crie um programa que leia quanto dinheiro uma
pessoa tem na carteira e mostre quantos dólares
ela pode comprar.

Considere
US$1.00 = 3.27
'''

reais = int(input('Digite um valor em reais: '))

print('{} reais é igual à US${}'.format(reais, reais*3.27))


