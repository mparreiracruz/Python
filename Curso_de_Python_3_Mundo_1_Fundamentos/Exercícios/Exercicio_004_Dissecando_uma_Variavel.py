'''
Exercício 004

Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo e todas as informações
possíveis sobre ela.
'''

valor = input("Digite algo: ")
print("O tipo primitivo de {} é ".format(valor), type(valor))
print("Só tem espaços ?", valor.isspace())
print("É um número ?", valor.isnumeric())
print("É alfabético ?", valor.isalpha())
print("É alfanumérico ?", valor.isalnum())
print("Está em maiúscula ?", valor.isupper())
print("Está em minúscula ?", valor.islower())
print("Está capitalizada ?", valor.istitle())

