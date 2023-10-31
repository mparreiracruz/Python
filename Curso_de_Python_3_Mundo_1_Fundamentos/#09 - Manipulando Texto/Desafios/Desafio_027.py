'''
Desafio 027

Faça um programa que leia o nome completo
de uma pessoa monstrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''

nome_completo = input("Escreva seu nome completo: ")

palavras = nome_completo.split()

primeiro_nome = palavras[0]
ultimo_nome = palavras[-1]

print("Primeiro nome: ", primeiro_nome)
print("Último nome: ", ultimo_nome)

