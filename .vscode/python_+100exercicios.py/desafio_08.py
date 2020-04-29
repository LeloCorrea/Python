'''Desafio 8 :
Escreva um programa que leia um valor em metros e exiba ele convertido em centímetros e milímetros.
'''

metros = float(input('Digite um valor em metros: '))
centimetros = int(metros * 100)
milimetros = int(metros * 1000)
#Para mostrar valores com ponto flutuante é preciso usar {:.2f}
print('O valor que você digitou foi: {:.2f} metros que possuem: {} centimetros e {} milimetros.'.format(metros, centimetros, milimetros))