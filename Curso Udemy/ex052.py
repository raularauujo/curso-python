#Calculadora
import math
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite a operação (+-/*): ')
    num_1_float = 0
    num_2_float = 0
    numero_valido = True
    try:
       num_1_float = float(numero_1)
       num_2_float = float(numero_2)

    except:
        numero_valido = None

    if numero_valido is None:
        print('Algum dos seus números é inválido.') 
        
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos or len(operador) > 1:
        print('Seu operador é inválido ou existe mais de 1.')
        continue
    
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('O Código nunca deve chegar aqui.')
