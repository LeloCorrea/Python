Primeiros comandos de python.

Base teórica:

Escrevendo mensagem na tela:

Dados que são mensagens, tem delimitadores especiais.

O delimitador padrão do python pra isso são as aspas simples, ou duplas. A grande maioria das mensagens são usadas aspas simples.

No python 3.0 todos os comandos são funções, por isso todos os comandos tem que ter parenteses. Parentes podem ser usadas em qualquer função.

Comando print, é para escrever na tela.

print('Olá Mundo!') # Precisei das aspas por ser uma mensagem. Retorna a mensagem

print(7+4) #Números não vai aspas. Retorna 1

print('7'+'4') #Para juntar duas mensagens que estão entre aspas é só colocar + entre elas. No caso do python pode ser os simbolos + ou , .

*No python toda variavel é um objeto, e um objeto é mais do que uma variavel.

Variaveis de saída (Print significa escreva):
nome='Anderson'
idade=31
peso=92.5
print(nome,idade,peso)

Variáveis de entrada (Input significa leia):
nome=input('Qual o seu nome?) #Nome recebe o resultado do input de 'Qual o seu nome'
idade=input('Quantos anos você tem?)
peso=input('Qual o seu peso?)

>>> Feito no programa Idle:

Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.

>>> print('Olá Mundo!')
Olá Mundo!
>>> print(Olá Mundo)
SyntaxError: invalid syntax

>>> print(7+4)
11
>>> print('7'+'4')
74
>>> 7+4
11
>>> '7'+'4'
'74'
>>> print('Olá'+5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('Olá'+5)
TypeError: must be str, not int
>>> print('Olá',5)
Olá 5

>>> nome='Anderson'
>>> idade=31
>>> peso=92.5
>>> print(nome,idade,peso)
Anderson 31 92.5
>>> print(nome+idade+peso)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(nome+idade+peso)
TypeError: must be str, not int
>>> nome=input('Qual o seu nome?')
Qual o seu nome?Pedro
>>> idade=input('Quantos anos você tem?')
Quantos anos você tem?63
>>> peso=input('Qual o seu peso?')
Qual o seu peso?65
>>> print(nome,idade,peso)
Pedro 63 65
>>> 

O modo interativo do Idle serve para testes, para experimentos.
Para criar programas é preciso ir para o modo de scripts do idle.

Criando scripts em python(#Modo de criação de scripts no idle):
Vai na área de trabalho cria uma pasta com o nome: scripts_python
Vai no Idle > clica em File > New file
Insere o script:

Exmplo:
#Modo de criação de scripts no idle
nome=input('Qual o seu nome? ')
idade=input('Qual a sua idade? ')
peso=input('Qual o seu peso? ')
print(nome,idade,peso)

Salvar o arquivo teste02 dentro da pasta scripts_python
Dentro desse arquivo vai em Run > Run module

Desafios:
1: Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

Script:
"""Desafio 01:
1: Crie um script python que leia o nome de uma pessoa
e mostre uma mensagem de boas-vindas de acordo com o valor digitado."""
nome=input('Qual é o seu nome?')
print('Olá ',nome,'! Prazer em te conhecer!')

Retorno:
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: /home/anderson/Área de Trabalho/scripts_python/desafio_01.py ===
Qual é o seu nome?Anderson
Olá  Anderson ! Prazer em te conhecer!
>>> 

2: Crie um script python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

Script:
"""Desafio 2:
Crie um script python que leia o dia, o mês
e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada."""

dia=input('Dia =  ')
mes=input('Mês =  ')
ano=input('Ano =  ')
print('Você nasceu no dia ',dia,' de ',mes,' de ',ano,'. Correto?')

Retorno:
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: /home/anderson/Área de Trabalho/scripts_python/desafio_02.py ===
Dia =  01
Mês =  12
Ano =  1988
Você nasceu no dia  01  de  12  de  1988 . Correto?
>>> 

3:
Crie um script python que leia dois números e tente mostrar a soma entre eles.

Script:
'''Desafio 3:
Crie um script python que leia dois números e tente mostrar a soma entre eles.'''

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