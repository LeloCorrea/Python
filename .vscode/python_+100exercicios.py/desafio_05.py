'''Desafio 5 :
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.'''

num = int(input('Digite um número inteiro: '))
sucessor = num +1
antecessor = num - 1
print('O número que você digitou é: {}, o seu sucessor é: {}, e o seu antecessor é: {}.'.format(num, sucessor, antecessor))