n = float(input('Digite um valor: '))
print(type(n))
'''
Saída:
Digite um valor: 7
7.0
'''

n = bool(input('Digite um valor: '))
print(type(n)) #Com o type
'''
Saída:
Digite um valor: 7
<class 'bool'>
'''

#Com um valor dentro da variavel vira True, sem o valor vira False
n = bool(input('Digite um valor: '))
print((n)) #Sem o type
'''
Saída:
Digite um valor: 7
True
'''

#Para saber se é numero 
n = input('Digite algo:')
print(n.isnumeric())
'''
#Digitando: 7
Saída:
Digite um valor: 7
True

Digitando: Oi
Saída:
Digite algo:Oi
False
'''

#Para saber se é letra
n = input('Digite algo:')
print(n.isalpha())
'''
#Digitando: Oi
Saída:
Digite um valor: Oi
True

Digitando: Oi
Saída:
Digite algo:Oi
False
'''
