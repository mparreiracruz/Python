'''
Desafio 023

Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos digitos separados.

ex:
Digite um número: 1834

Unidade: 4
Dezena: 3
centena: 8
milhar: 1
'''

n = str(int(input("Digite um número: ")))

print("Unidade = ", n[3])
print("Dezena = ", n[2])
print("Centena = ", n[1])
print("Milhar = ", n[0])
