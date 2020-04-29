'''Desafio 11 :
Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m².

Calculando a área: área (m²) = lado (m) x lado(m)
Próxima melhoria para este programa:
Um galão de 3,6 l dá para pintar 18 m². Se for fazer duas demãos, dá para 9 m².

Um galão de 18 l dá para pintar 90 m². Se for fazer duas demãos, dá para 45 m².
'''
capacidadetinta = int(input('Qual a capacidade de pintura do Lt da tinta p/M²: '))
demaos = int(input('Quantas demãos de tinta você irá pintar: '))
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area  = largura * altura
demao = ((largura * altura)/demaos)
tinta = ((area / capacidadetinta)*demaos)
print('Area total é: {:.2f}m².\nEntão para uma area total de: {:.2f}m², você precisará {:.2f}Lt de tinta, considerando uma tinta que rende {}Lt p/m² pintando {} demão(s)'.format(area, area, tinta, capacidadetinta, demaos.))


'''print('A largura é: {} metros e a altura é: {} metros.\nArea total é: {:.2f}m².\nCada litro de tinta pinta uma área de {:.2f}m²\nEntão para uma area total de: {:.2f}m², você precisará {:.2f}Lt de tinta.\nCom {} demão(s) você conseguirá pintar uma área de {:.2f}m²'.format(largura, altura, area, capacidadetinta, area, tinta, demaos, demao))'''