'''
Desafio 017

Faça um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''

from math import sqrt, pow

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))

print('O comprimento da hipotenusa é : {:.3f}'.format(sqrt(pow(oposto, 2)+pow(adjacente, 2))))
