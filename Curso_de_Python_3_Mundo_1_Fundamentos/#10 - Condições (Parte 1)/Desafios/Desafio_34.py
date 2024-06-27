'''
Desafio 034

Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento
de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Digite o seu salário: '))

if salario > 1.250:
    aumento_10_por_cento = salario * 1.10
    print('Seu novo salário é: R${:.2f}'.format(aumento_10_por_cento))
else:
    aumento_15_por_cento = salario * 1.15
    print('Seu novo salário é: R${:.2f}'.format(aumento_15_por_cento))