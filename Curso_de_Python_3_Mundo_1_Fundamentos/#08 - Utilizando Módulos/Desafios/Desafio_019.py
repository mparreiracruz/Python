'''
Desafio 019

Um professor quer sortear um dos seus quatros alunos
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.
'''
from random import choice

nome1 = input('Digite o seu nome: ')
nome2 = input('Digite o seu nome: ')
nome3 = input('Digite o seu nome: ')
nome4 = input('Digite o seu nome: ')

nomes = [nome1, nome2, nome3, nome4]

escolhido = choice(nomes)

print('O nome escolhido é ', escolhido)
