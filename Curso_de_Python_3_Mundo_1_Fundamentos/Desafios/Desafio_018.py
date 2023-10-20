'''
Desafio 018

Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
'''
from math import radians, sin, cos, tan

#Método 01
'''angulo = float(input('Digite um ângulo: '))

angulo = radians(angulo)

print('O seno é {:.4f}\nO cosseno é {:.4f}\nA tangente é {:.4f}'.format(sin(angulo), cos(angulo), tan(angulo)))
'''

#Método 02
angulo = float(input('Digite um ângulo: '))

seno = sin(radians(angulo))
print("O SENO é de {:.2f}".format(seno))

cosseno = cos(radians(angulo))
print("O COSSENO é de {:.2f}".format(cosseno))

tangente = tan(radians(angulo))
print("A Tagente é de {:.2f}".format(tangente))
