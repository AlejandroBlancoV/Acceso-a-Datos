euros=0
tasaCambio=0 
while euros<=0:
    euros=float(input("Introduce la cantidad de euros: "))
    if euros<=0:
        print("La cantidad de euros debe ser mayor que 0")
while tasaCambio<=0:
    tasaCambio=float(input("Introduce la tasa de cambio: "))
    if tasaCambio<=0:
        print("La tasa de cambio debe ser mayor que 0")

enDolares=float(euros)*float(tasaCambio)
print(str(euros)+" euros son "+str(enDolares)+" dólares")