#Exercício
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
if idade and nome:
    print('Seu nome é {}'.format(nome))
    print('Seu nome invertido é: "{}"'.format(nome[::-1]))
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
    
        print('Seu nome NÃO contém espaços')

    print('Seu nome tem {} letras'.format(len(nome)))
    print('A primeira letra do seu nome é "{}"'.format(nome[0]))
    print('A última letra do seu nome é "{}"'.format(nome[-1]))
else:
    print('Você deixou campos vazios.')
