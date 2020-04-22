'''3:
Crie um script python que leia dois números e tente mostrar a soma entre eles.

Script:
Desafio 3:
Crie um script python que leia dois números e tente mostrar a soma entre eles.

num1=input('Primeiro número: ')
num2=input('Segundo número: ')
print('A soma é ', num1 + num2)

Retorno: #Deu erro, a resposta estará na próxima aula.
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: /home/anderson/Área de Trabalho/scripts_python/desafio-03.py ===
Primeiro número: 6
Segundo número: 3
A soma é  63
>>>
'''

#Resposta correta
n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
resultado = n1+n2
print('O resultado da soma entre n1 e n2 é: {}'.format(resultado))