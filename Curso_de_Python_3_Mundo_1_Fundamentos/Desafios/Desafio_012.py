'''
Desafio 012

Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
'''

produto = int(input('Digite o valor do produto: R$'))

desconto = produto - (produto * 0.05)

print('{} reais com 5% de desconto é igual à: {:.2f} reais'.format(produto, desconto))
