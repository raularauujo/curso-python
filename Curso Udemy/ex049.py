contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Maracujá')
        continue
    
    if contador >= 10 and contador <=30:
        print('Goiaba', contador)
        continue


    if contador == 40:
        print('Suco de Uva', contador)
    print(contador)

    if contador == 99:
        break