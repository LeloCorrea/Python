'''Desafio 11 original:
Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m².

Calculando a área: área (m²) = largura (m) x altura(m)
OBS.: Mudanças que eu fiz em relação ao programa original:
1 - Solicitei a capacidade da tinta.
2 - Solicitei o número de demãos que serão dadas na parede.
3 - Solicitei a largura x altura, para termos a área total.
4 - Apresentei os dados.
'''
capacidadetinta = int(input('Qual a capacidade de pintura do Lt da tinta p/M²: '))
demaos = int(input('Quantas demãos de tinta você irá pintar: '))
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area  = largura * altura
demao = ((largura * altura)/demaos)
tinta = ((area / capacidadetinta)*demaos)
print('Sua parede tem a dimensão de {}x{} e sua area total é: {:.3f}m².\nEntão para uma area total de: {:.3f}m², você precisará {:.2f}Lt de tinta, considerando uma tinta que rende {}Lt p/m², pintando {} demão(s)'.format(largura, altura, area, area, tinta, capacidadetinta, demaos))


'''print('A largura é: {} metros e a altura é: {} metros.\nArea total é: {:.2f}m².\nCada litro de tinta pinta uma área de {:.2f}m²\nEntão para uma area total de: {:.2f}m², você precisará {:.2f}Lt de tinta.\nCom {} demão(s) você conseguirá pintar uma área de {:.2f}m²'.format(largura, altura, area, capacidadetinta, area, tinta, demaos, demao))'''