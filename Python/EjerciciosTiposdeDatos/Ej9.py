dinero=float(input('Introduce el dinero a invertir'))
interes=float(input('Introduce el interés anual'))
años=float(input('Introduce los años'))

total=(((dinero*interes)/100)*años)+dinero
print('Total a recibir',total)
