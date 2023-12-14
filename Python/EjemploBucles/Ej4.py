numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("El número debe ser positivo.")
else:
    countdown = ""
    for i in range(numero, -1, -1):
        countdown += str(i) + ","
    
    print(countdown[:-1])  # Eliminar la última coma
