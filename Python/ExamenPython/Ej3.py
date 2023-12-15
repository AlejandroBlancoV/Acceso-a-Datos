precio=0
descuento=0
while precio<=0:
    precio=float(input("Introduce el precio original del producto: "))
    if precio<=0:
        print("El precio debe ser mayor que 0")

while descuento<=0:
    descuento=float(input("Introduce el porcentaje de descuento: "))/100
    if descuento<=0:
        print("El porcentaje de descuento debe ser mayor que 0")

precioFinal=precio-(precio*descuento)
print("El precio final con descuento  es "+str(precioFinal))
