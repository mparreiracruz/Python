from random import randint
from time import sleep

'''
Desafio 028

Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''

'''
n = int(input('Digite um número inteiro entre 0 e 5 que pode ter sido escolhido pela máquina: '))

num = randint(0, 5)
print(num)

if n == num:
    print('Parabéns, voce acertou!')
else:
    print('Voce perdeu.')
'''

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
print('PROCESSANDO...')
sleep(3)

jogador = int(input('Em que número eu pensei ? '))
if jogador == computador:
    print('Parabéns! Voce conseguir me vencer !')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
