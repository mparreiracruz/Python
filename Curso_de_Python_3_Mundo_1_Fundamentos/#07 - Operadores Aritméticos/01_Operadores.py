'''
Curso Python #07 - Operadores Aritméticos

Nessa aula, vamos aprender quais são os operadores aritméticos
do Python e também sua ordem de precedência dentro de
expressões matemáticas.
Veja como funcionam os operadores de adição, subtração, multiplicação,
divisão, exponenciação e quociente na linguagem Python.

Ordem de Precedência

1 ()
2 **
3 *   /   //   %
4 +   -
'''
#nome = input('Qual o seu nome ? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 / n2
e = n1 ** n2
#print('Soma vale {}'.format(n1+n2))
print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end='')
print('A divisão inteira é {} e a potência é {}'. format(di, e))
