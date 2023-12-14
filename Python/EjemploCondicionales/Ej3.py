# Pedir al usuario dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Verificar si el divisor es cero
if num2 == 0:
    print("Error: No se puede dividir entre cero")
else:
    # Calcular la división
    division = num1 / num2
    print("El resultado de la división es:", division)
