n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua média é {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi ótima')
else:
    print('Sua média foi horrível')