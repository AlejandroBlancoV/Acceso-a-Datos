precioNormal=3.49
descuento=0.6
precioDescuento=precioNormal*descuento
numeroBarras=int(input("Introduce el número de barras vendidas que no son del día: "))
print("Precio habitual: "+str(precioNormal))
print("Descuento: "+str(descuento))
print("Precio por barra: "+str(precioDescuento))
print("Coste final: "+str(numeroBarras*precioDescuento))
