'''
Desafio 005

Faça um programa que leia um número
inteiro e mostre na tela o seu sucessor e
seu antecessor.
'''

n = int(input('Digite um número inteiro: '))

s = n + 1
a = n - 1

print('O sucessor de {} é {}, e seu antecessor é {}'.format(n, s, a))

