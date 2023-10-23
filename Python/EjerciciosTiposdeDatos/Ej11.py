interes=0.04
inversionIncial=float(input('Introduce la cantidad a depositar'))
años=1
inversionFinal=inversionIncial
while años<=3:
    inversionFinal+= (inversionFinal*interes)
    print('año',años,': ', round( inversionFinal,2)  )
    años+=1
