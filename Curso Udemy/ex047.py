"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = (input('Digite um número inteiro: '))
if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'
    print('O número {} é {}.'.format(numero_int, par_impar_texto))
else:
    print('O número digitado não é inteiro.')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = (input('Que horas são? '))
try:
    hora = int(horario)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, apenas números inteiros.')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Qual o seu nome? ')
tamanho_do_nome = len(nome)
if tamanho_do_nome > 1:
    if tamanho_do_nome <= 4:
        print('Nome curtinho né')
    if tamanho_do_nome >= 5 and tamanho_do_nome <= 6:
        print('Seu nome ta na média de tamanho')
    else:
        print('Nome grande da #####')
else:
    print('Digite mais de uma letra.')