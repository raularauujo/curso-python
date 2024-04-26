# Curso em vídeo
salario = float(input('Digite qual o salário do funcionário: '))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('O salário que antes era R${:.2f}, agora é R${:.2f}'.format(salario, aumento))

# Curso udemy a partir daqui:
entrada = input('Você quer "entrar", ou "sair"? ')
if entrada == 'entrar':
    print('Você entrou no sistema.')
elif entrada == 'sair':
    print('Você saiu do sistema.')
else:
    print('Você não digitou nem entrar e nem sair.')