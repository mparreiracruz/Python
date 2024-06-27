'''
Desafio 027

Faça um programa que leia o nome completo
de uma pessoa monstrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''

'''
#Alternativa
nome_completo = input("Escreva seu nome completo: ")

palavras = nome_completo.split()

primeiro_nome = palavras[0]
ultimo_nome = palavras[-1]

print("Primeiro nome: ", primeiro_nome)
print("Último nome: ", ultimo_nome)
'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'. format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

