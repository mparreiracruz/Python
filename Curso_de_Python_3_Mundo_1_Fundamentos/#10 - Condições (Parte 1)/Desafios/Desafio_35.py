'''
Desafio 035

Desenvolva um programa que leia o comprimento de tres retas
e diga ao usuário se eles podem ou não formar um triangulo.
'''

reta1 = float(input('Digite o primeiro comprimento: '))
reta2 = float(input('Digite o segundo comprimento: '))
reta3 = float(input('Digite o terceiro comprimento: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Forma um triangulo.')
else:
    print('Não forma um triangulo.')