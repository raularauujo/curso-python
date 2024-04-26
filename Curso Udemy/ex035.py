# Curso em vídeo
print('-=-'*8)
print('Analisador de Triângulos')
print('-=-'*8)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
# :)
# Curso udemy a partir daqui
condicao = True
if condicao:
    print('Este é o código if')
else:
    print('Esse é o código do else')
print('Fora do if')
