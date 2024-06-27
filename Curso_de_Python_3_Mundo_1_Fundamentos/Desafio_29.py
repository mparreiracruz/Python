'''
Desafio 029

Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

'''
velocidade_carro = float(input('Digite a velocidade do seu carro: '))

if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 7
    print('Voce foi multado no valor de R${:.2f} !'.format(multa))
else:
    print('Voce está na velocidade permitida.')
'''

velocidade_carro = float(input('Digite a velocidade do seu carro: '))

if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 7
    print('Voce foi multado no valor de R${:.2f} !'.format(multa))

print('Voce está na velocidade permitida.')


