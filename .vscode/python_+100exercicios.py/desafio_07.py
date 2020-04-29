'''Desafio 7 :
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''
nome = str(input('Digite o nome do aluno: '))
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = ((nota1 + nota2) / 2)
print('O aluno: {}, tem a seguinte média: {}.\n(Pois a primeira nota foi: {} e a segunda nota foi:{} ).'.format(nome,media,nota1,nota2))