'''Desafio 8 :
Escreva um programa que leia um valor em metros e exiba ele convertido em centímetros e milímetros.
'''

medida = float(input('Digite um valor em metros: '))
centimetros = medida * 100
milimetros = medida * 1000
#Para mostrar valores com ponto flutuante é preciso usar {:.2f}
print('A medida de{}m corresponde a {:.0f}cm e {:.0f}mm.'.format(medida, centimetros, milimetros))