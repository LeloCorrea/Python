'''Trabalhando com módulos:

Teoria:
Os programas em python por padrão tem um conjunto limitado de programas, isso é feito para que a linguagem seja rápida e os programas sejam pequenos e não gastem memória. Se for preciso algumas funcionalidades é preciso importar, através de bibliotecas.

Duas maneiras basicas para importar módulos dentro de python:
    Exemplo de comandos (import e from import):
        import bebida(agua,suco,café,refrigerante)  #Traz todas as bebidas da biblioteca bebida
        from bebida import café

Biblioteca padrão de python:
    math
        Funcionalidades:
            ceil        # Faz um arredondamento pra cima
            floor       # Faz um arredondamento para baixo
            trunc       # Elimina da virgula pra frente, truncando  
            pow         # Potencia
            sqrt        # Raiz Quadrada
            factorial   # Fatorial

import math #Importa tudo que tem dentro da biblioteca, podendo utilizar todas as funcionalidades

from math import sqrt, ceil   #Importa só a funcionalidade de raiz quadrada e ceil da biblioteca.