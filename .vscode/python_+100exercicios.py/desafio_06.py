'''Desafio 6 :
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada:
'''
'''
#Primeira maneira de fazer
num = int(input('Digite um número: '))
dobro = num*2
triplo = num*3
raiz = num**(1/2) #Raiz representada através de exponenciação (num elevado a meio)
print('O número que você digitou é: {}\nO seu dobro é: {}\nO seu triplo é: {}\nA sua raiz quadrada é: {:.2f}.'.format(num, dobro, triplo, raiz))
'''

#Outra maneira de fazer
n = int(input('Digite um número: '))
print('O número que você digitou é: {}\nO seu dobro é: {}\nO seu triplo é: {}\nSua raiz é: {:.2f}.'.format(n, n*2, n*3, pow(n,1/2))) #Utilizando a função pow.