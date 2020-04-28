'''Desafio 04:
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

algo = input('Digite algo: ')
print('Você digitou: {}'.format(algo))
print('O tipo primitivo deste valor é: ', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É um alfabético?', algo.isalpha())
print('É um alfanumérico?', algo.isalnum())
print('Esta em maiúsculas?', algo.isupper())
print('Esta em minúsculas?', algo.islower())
print('Esta em capitalizada?', algo.istitle())


#A função input retorna sempre uma string.
