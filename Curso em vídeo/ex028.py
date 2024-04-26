from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'*16)
print('Pensei em um número entre 0 e 5, tente advinhar:')
print('-=-'*16)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2.5)
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Eu ganhei, eu pensei no número {}'.format(computador))
