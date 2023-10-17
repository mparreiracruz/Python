'''
Desafio 018

Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
'''
from math import radians, sin, cos, tan, ceil

angulo = float(input('Digite um ângulo: '))

angulo = radians(angulo)

print('O seno é {:.4f}, seu cosseno é {:.4f} e sua tangente é {:.4f}'.format(sin(angulo), cos(angulo), tan(angulo)))
