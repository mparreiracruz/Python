'''
Desafio 026

Faça um programa que leia uma frase pelo teclado
e mostre:

>Quantas vezes aparece a letra "A".

>Em que posição ela aparece a primeira vez.

>Em que posição ela aparece a última vez.
'''

frase = input('Digite uma frase: ')

frase_sem_espaco = frase.replace(' ', '')

print('Nessa frase a letra "a" aparece', frase_sem_espaco.lower().count('a'), 'vezes.')
print('Nessa frase a letra "a" aparece pela primeira vez na posição', frase_sem_espaco.lower().find('a'))
print('Nessa frase a letra "a" aparece pela última vez na posição', frase_sem_espaco.lower().rfind('a'))
