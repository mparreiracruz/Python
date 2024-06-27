'''
Desafio 031

Desenvolva um programa que pergunte a distancia de uma viagem
em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 para viagens mais longas.

'''

distancia = float(input('Digite a distancia da sua viagem em quilometros: '))

if distancia <= 200:
    preco_passagem_curta = distancia * 0.50
    print('Preço da passagem: R${:.2f}'.format(preco_passagem_curta))
if distancia > 200:
    preco_passagem_longa = distancia * 0.45
    print('Preço da passagem: R${:.2f}'. format(preco_passagem_longa))
