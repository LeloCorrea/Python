'''Desafio 15:
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.'''

tempoAluguel = int(input('Por quantos dias você alugou o carro? '))
percurso = float(input('Quantos KM você rodados com o carro? '))
dividaDiarias = tempoAluguel * 60
dividaPercurso = percurso * 0.15
total = dividaDiarias + dividaPercurso
print('Você alugou o carro por {} dias, com isso o valor total das diárias é R${:.2f}.\nTendo feito um percurso de {}KM o valor a ser pago é R${:.2f}.\nO total a pagar é R${:.2f}.'.format(tempoAluguel, dividaDiarias, percurso, dividaPercurso, total))