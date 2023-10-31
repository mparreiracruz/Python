'''
Desafio 024

crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "SANTO".
'''

cidade = input("Digite o nome da sua cidade: ")


if cidade.find('santo') == 0:
    print("Sua cidade começa com o nome Santo.")
else:
    print("Sua cidade não começa com o nome Santo.")
