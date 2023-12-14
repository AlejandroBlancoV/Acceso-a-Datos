# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero <= 0:
    print("El número debe ser positivo.")
else:
    # Inicializar una lista para almacenar los números impares
    impares = ""

    # Iterar desde 1 hasta el número ingresado, incluyendo el número ingresado
    for i in range(1, numero + 1):
        # Verificar si el número es impar
        if i % 2 != 0:
            # Agregar el número a la lista de impares
            impares+=str(i)+","

    # Imprimir los números impares separados por comas
    print(impares[:-1])
