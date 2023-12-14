# Pedir al usuario la cantidad a invertir, el interés anual y el número de años
cantidad = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual en porcentaje: "))
num_anios = int(input("Ingrese el número de años de la inversión: "))

# Calcular el capital obtenido en la inversión cada año
for i in range(1, num_anios + 1):
    capital_obtenido = cantidad * (1 + interes_anual / 100) ** i
    print(f"Año {i}: {capital_obtenido}")
