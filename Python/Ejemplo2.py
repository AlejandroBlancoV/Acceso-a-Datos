temperatura=int(input('Introduzca temperatura'))
if temperatura < 20:
    if temperatura < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperatura <30:
        print('Nivel naranja')

    else :
        print('Nivel rojo')
