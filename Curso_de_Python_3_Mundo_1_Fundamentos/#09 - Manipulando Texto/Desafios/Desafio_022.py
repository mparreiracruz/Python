'''
Desafio 022

Crie um programa que leia o nome completo de uma
pessoa e mostre:

>O nome com todas as letras maiúsculas

>Quantas letras ao todo(sem considerar espaços).

>Quantas letra tem o primeiro nome.
'''

nome = input('Digite o seu nome: ')

print('Em letra maiúscula: ', nome.upper())

contador_sem_espaco = nome.replace(" ", "")

primeiro_nome = nome.split()

primeira_nome_numero_de_letras = primeiro_nome[0]

print('Número de letras sem contar o espaço: ', len(contador_sem_espaco))
print("Número de letras do primeiro nome: ", len(primeira_nome_numero_de_letras))





