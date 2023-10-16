'''
Desafio 015

Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa
R$60 por dia e R$0.15 por km rodado.
'''
diasalugados = int(input('Quantidade de dias: '))
kmpercorridos = float(input('Km percorridos: '))


precoapagar = (diasalugados * 60) + (kmpercorridos * 0.15)

print('Preço a pagar: R${:.2f}'.format(precoapagar))
