'''
Desafio 025

Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome.
'''

nome = input("Digite seu nome: ")

if 'silva' in nome.lower():
    print('Seu nome tem o nome "Silva".')
else:
    print('Seu nome não tem o nome "Silva".')
