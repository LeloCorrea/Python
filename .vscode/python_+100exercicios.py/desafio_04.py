'''Desafio 04:
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

algo = input('Digite algo: ')
print('Você digitou: {}'.format(algo))
print('E {} é um(a) tipo:'.format(algo))
print(type(algo))