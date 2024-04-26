#Debugger 
"""""
O debugger básicamente executa o código inteiro passo a passo e te mostra como o programa
está interpretando o código para te ajudar a resolver erros
"""""
import random
print('Se você tirar o mesmo número 2 vezes você perdeu')
x = random.randint(1,25)
y = random.randint(1,25)
print('Primeiro número é {}, o segundo escolhido foi {}.'.format(x, y))
if x == y:
    print('PERDEU VACILÃO')
else:
    print('Na próxima eu te pego')
#Código de exemplo pra debugar
    