'''
O mesmo professor do desafio anterior quer sortear
a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatros
alunos e mostre a ordem sorteada.
'''

from random import shuffle

nome1 = str(input('Digite o seu nome: '))
nome2 = str(input('Digite o seu nome: '))
nome3 = str(input('Digite o seu nome: '))
nome4 = str(input('Digite o seu nome: '))

nomes = [nome1, nome2, nome3, nome4]

shuffle(nomes)

print('A ordem dos nomes escolhidos é: ', nomes)
