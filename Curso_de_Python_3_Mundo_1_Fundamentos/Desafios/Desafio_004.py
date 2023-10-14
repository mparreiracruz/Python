'''
Desafio 04

Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possíveis sobre
ele(se é um numero, se é alfabético etc).
'''

tipo = input("Digite qualquer coisa: ")

print('{} é'.format(tipo), 'numérico ?', tipo.isnumeric(), '\n{} é alfabético ?'.format(tipo), tipo.isalpha())
print('{} pode ser impresso ?'.format(tipo), tipo.isprintable())
