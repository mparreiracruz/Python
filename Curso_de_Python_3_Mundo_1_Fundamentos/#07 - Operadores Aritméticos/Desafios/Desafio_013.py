'''
Desafio 013

Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário com 15% de
aumento.
'''

salario = int(input('Digite o valor do seu salário: '))

aumento = salario * 0.15
novosalario = salario + aumento

print('O seu novo salário é: {} reais'.format(novosalario))
