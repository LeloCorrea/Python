'''Desafio 16:
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex: Digite um número 6.127.
O número 6.127 tem a parte inteira 6.
'''
'''
#Primeira maneira:
#import math
from math import trunc
numero = float(input('Digite um número: '))
print('O valor digitado é: {} e a sua porção inteira é: {}.'.format(numero, math.trunc(numero)))
'''
'''
#Segunda maneira:
from math import trunc
numero = float(input('Digite um número: '))
print('O valor digitado é: {} e a sua porção inteira é: {}.'.format(numero, trunc(numero)))
'''

#Terceira maneira:
num = float(input('Digite um valor: '))
print('O valor digitado é: {} e a sua porção inteira é: {}.'.format(numero,int(num)))
