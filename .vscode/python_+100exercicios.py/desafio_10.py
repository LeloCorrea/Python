'''Desafio 10 :
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considerando 1 dolar  = 5.50 (28/04/2020).
'''
real = float(input('Digite quanto dinheiro você tem na carteira: R$'))
dollares = real / 5.50
#Como estou usando float quero ver apenas duas casas depois da virgula com o {:.2f}.
print('Com este dinheiro: R${:.2f}, você consegue comprar ${:.2f} no dia de hoje (28/04/2020).'.format(real, dollares))