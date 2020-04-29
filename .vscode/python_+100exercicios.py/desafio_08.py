'''Desafio 8 :
Escreva um programa que leia um valor em metros e exiba ele convertido em centímetros e milímetros.
'''

metros = float(input('Digite um valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print('O valor que você digitou foi: {} metros que possuem: {} centimetros e {} milimetros.'.format(metros, centimetros, milimetros))