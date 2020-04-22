#Verificando tipos primitivos de variaveis, utilizando o type:
n1 = input('Digite um valor:')
print(type(n1))
'''Saída: 
    Digite um valor:7
    <class 'str'>
'''

n1 = int(input('Digite um valor:'))
print(type(n1))
'''
Saída:
    Digite um valor:7
    <class 'int'>
'''

#Lembrando ao declarar uma variável é preciso sempre declarar o tipo de variável

'''
n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
# Se não for declarado o tipo de variável o + servirá como concatenação.
s=n1+n2'''

n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s = n1+n2
#Melhor formato de print para python, utilizando o metodo .format, que serve para qualquer tipo primitivo de variável:
print('O resultado entre {} e {} é {}'.format(n1, n2, s))
'''
Saída:
Digite um valor: 1
Digite outro valor: 2
O resultado entre 1 e 2 é 3
'''