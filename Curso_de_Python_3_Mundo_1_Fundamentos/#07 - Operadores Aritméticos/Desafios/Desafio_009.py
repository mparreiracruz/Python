'''
Desafio 009

Faça um programa que leia um número inteiro
qualquer e mostre sua tabuada.
'''

n = int(input('Digite um número inteiro: '))

for tabuada in range(1, 11):
    resultado = n * tabuada
    print('{} x {} = {}'.format(n, tabuada, resultado))
