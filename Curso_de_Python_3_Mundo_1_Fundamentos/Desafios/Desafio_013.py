'''
Desafio 013

Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário com 15% de
aumento.
'''

salario = float(input('Digite o valor do seu salário: R$'))

aumento = salario + (salario * 0.15)

print('O seu novo salário é de {:.2f} reais'.format(aumento))
