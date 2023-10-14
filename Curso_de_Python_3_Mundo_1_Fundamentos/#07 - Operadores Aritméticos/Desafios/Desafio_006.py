'''
Desafio 006

Crie um algoritmo que leia um número
e mostre o seu dobro, triplo e a raiz quadrada.
'''

n = int(input('Digite um número inteiro: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro desse número é: {}'.format(n*2), '\nO triplo desse número é: {}'.format(n*3))
#print('A raiz quadrada desse número é: {:.2f}'.format(n**0.5))

print('A raiz quadrada desse número é: {:.2f}'.format(pow(n, (1/2))))

#print('O dobro de {} é {}'.format(n, d))
#print('O triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}.'.format(n, t, n, r))
