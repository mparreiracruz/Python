'''
Desafio 017

Faça um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''

from math import sqrt, pow
from math import hypot

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))

#Método 01
#hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
#print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))

#Método 02
#print('O comprimento da hipotenusa é: {:.2f}'.format(sqrt(pow(oposto, 2)+pow(adjacente, 2))))

#Método 03
hipotenusa = hypot(oposto, adjacente)
print("O comprimento da hipotenusa é: {:.2f}".format(hipotenusa))


