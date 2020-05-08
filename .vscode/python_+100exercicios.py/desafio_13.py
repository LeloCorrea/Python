'''Desafio 13 :
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
salario = float(input('Qual o salário do funcionário? '))
aumento = 15 #por cento
novoSalario = salario + ((salario * aumento)/100)
aumentoReal = novoSalario - salario
print('O funcionário tem o salario de:R${:.2f}, com um aumento de {}% o salário atual passou a ser: R${:.2f}.\nCom isso o funcionário teve um aumento real de: R${:.2f} no seu salário.'.format(salario, aumento, novoSalario, aumentoReal))