'''Desafio 12 :
Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
'''
produto = float(input('Digite o preço de um produto: R$'))
desconto = 5
economia = ((produto * desconto)/100)
valorreal = produto - economia
print('O produto tem o valor de: R$ {:.2f}, com 5% de desconto fica: R${:.2f}.\nVocê teve uma economia de: R${:.2f}.'.format(produto, valorreal, economia))
