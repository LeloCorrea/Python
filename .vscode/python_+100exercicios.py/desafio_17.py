'''Desafio 17:
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

O quadrado da hipotenusa é igual a soma dos quadrados dos catetos.
'''
'''
#Maneira tradicional matematicamente falando
catetoOposto = float(input('Digite o comprimento to cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (catetoOposto **2 + catetoAdjacente **2) ** (1/2)
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))
'''
'''
import math
catetoOposto = float(input('Digite o comprimento to cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catetoOposto,catetoAdjacente)
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))
'''
from math import hypot
catetoOposto = float(input('Digite o comprimento to cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(catetoOposto,catetoAdjacente)
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))