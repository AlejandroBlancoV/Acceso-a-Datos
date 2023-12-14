income = float(input("Ingrese su renta anual: "))

if income < 10000:
    tax_rate = 0.05
elif income < 20000:
    tax_rate = 0.15
elif income < 35000:
    tax_rate = 0.20
elif income < 60000:
    tax_rate = 0.30
else:
    tax_rate = 0.45

print("El tipo impositivo correspondiente es:", tax_rate*100+str('%'))
