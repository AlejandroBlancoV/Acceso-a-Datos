nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
numero_unidades = int(input("Ingrese el número de unidades: "))

coste_total = precio_unitario * numero_unidades

cadena_resultado = f"Producto: {nombre_producto}\n"
cadena_resultado += f"Precio unitario: {precio_unitario:6.2f}\n"
cadena_resultado += f"Número de unidades: {numero_unidades:3d}\n"
cadena_resultado += f"Coste total: {coste_total:8.2f}"

print(cadena_resultado)
