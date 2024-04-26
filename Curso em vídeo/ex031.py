passagem = float(input('Quantos KM terá sua viagem? '))
if passagem <= 200:
    print('O valor da sua viagem, é de R${:.2f}'.format(passagem * 0.50))
else:
    print('O valor da sua viagem, é de R${:.2f}'.format(passagem * 0.45))
