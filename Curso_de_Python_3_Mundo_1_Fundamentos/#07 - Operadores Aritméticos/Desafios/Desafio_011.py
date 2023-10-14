'''
Desafio 011

Faça um programa que leia a largura e a altura
de uma parede em metros. Calcule a sua área e a
quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área
de 2m².
'''

largura = int(input('Digite a largura da sua parede: '))
altura = int(input('Digite a altura da sua parede: '))

area = largura*altura

print('Area = {}\nSerá necessário {} litros de tinta.'.format(area, (area/2)))
#print('Área = {}\nSerá necessário {} litros de tinta.'.format(largura*altura, ((largura*altura)/2)))
