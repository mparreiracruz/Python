#import math
from math import sqrt, floor

num = int(input('Digite um número inteiro: '))

raiz = sqrt(num)

print('A raiz de {} é {}'.format(num, floor(raiz)))
#print('A raiz de {} é {}'.format(num, math.ceil(raiz)))
#print('A raiz de {} é {:.2f}'.format(num, raiz))
