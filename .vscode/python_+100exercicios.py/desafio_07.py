'''Desafio 7 :
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''
nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = ((nota1 + nota2) / 2)
print('O aluno: {}, tem a seguinte média: {:.1f}\n(Pois a primeira nota foi: {:.1f} e a segunda nota foi: {:.1f})'.format(nome,media,nota1,nota2))