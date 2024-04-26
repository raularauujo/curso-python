velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO!, você excedeu o limite permitido de 80km/h!')
    multa = (velocidade-80) * 7
    print('Sua multa é de R${:.2f}'.format(multa))
else:
    print('Você está no limite de velocidade permitida.')
print('Tenha um bom dia! Dirija com segurança!')