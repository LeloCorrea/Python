'''Desafio 003:
Crie um programa que leia dois números e mostre a soma entre eles:'''

#É preciso colocar o tipo da variável que você quer que apareça antes do input.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = num1+num2

print("A soma entre {} e {} é {}!".format(num1, num2,resultado)) 
#É preciso colocar dentro do comando format as variáveis na ordem que você quer que apareça.
