'''Utilizando os operadores aritmeticos na prática. 

No console:
>>>5+3*2 #Primeiro faz a multiplicação e depois a soma
11

>>> 5**2 #Valor ao quadrado
25

>>> 5**3 #valor ao cubo
125

>>> 19//2 #Divisão inteira
9

>>> 19/2 #Divisão real

>>> 365**522 #Em python o limite é o tamanho da memória.
32875717981981342289734219608076461210798383174338902362440525567069083206084822182430672
...

>>> 18%2 #Resto da divisão
0

>>> 122%3
2

>>> 4**3 #Ao cubo
64
>>> pow(4,3) # Usando função
64

>>> 1/2 #Raiz quadrada de um valor
0.5
>>> 81**(1/2) #Faz a divisão de 1/2 = 0.5, pega o valor e eleva a 0.5
9.0
>>> 25**(1/2)
5.0

>>> 127**(1/3) #Raiz cúbica
5.026525695313479

>>> 'Oi' + 'Ola' # Concatena
'OiOla'

>>> 'Oi' * 5 #Multiplica o conjunto de strings
'OiOiOiOiOi'

>>> '='*20
'===================='

>>> print('='*20)
====================
'''

'''
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer, {:^20}!'.format(nome))
#Tipos de alinhamento: {:>20}, {:<20}, {:^20}, {:=^20}
'''
'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale: {}'.format(n1+n2))
'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2  #Adição
subt = n1 - n2  #Subtração
mult = n1 * n2  #Multiplicação
divi = n1 / n2  #Divisão real
dint = n1 // n2 #Divisão inteira
expo = n1 ** n2 #Exponenciação

print('A soma é: {} \nA subtração é: {}'.format(soma, subt))
print('O produto/multiplicação é: {} \nA divisão real é: {}'.format(mult, divi))
print('A divisão inteira é: {} \nA exponenciação é: {}'.format(dint, expo))
 
  