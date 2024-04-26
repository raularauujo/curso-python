import random
print('Você vai assistir AIB hoje?')
x = random.randint(1,24)
y = random.randint(1,24)
print('Primeiro número é {}, o segundo escolhido foi {}.'.format(x, y))
if x == y:
    print('É hoje que você vai ver esse negócio')
else:
    print('Mais um dia com o cérebro intacto')
