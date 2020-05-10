''' Importando todas as funcionalidades da biblioteca math:

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de um {} é igual a {:.2f}'.format(num,raiz))

#Outras maneiras de mostrar o valor
print('A raiz de um {} é igual a {}'.format(num, math.floor(raiz)))

print('A raiz de um {} é igual a {}'.format(num, math.ceil(raiz)))
'''
'''
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de um {} é igual a {:.2f}'.format(num,raiz))

from math import sqrt,floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de um {} é igual a {:.2f}'.format(num, floor(raiz)))
'''
#O metodo random da classe random gera um numero aleatorio entre 0 e 1, um numero float, um numero real.
import random
num = random.random() #
#O randint, gera um numero inteiro de 1 até 10
numint = random.randint(1,10)
print(num)
print(numint)

#Para ter acesso a mais bibliotecas para importação: import + ctrl + espaço
import emoji