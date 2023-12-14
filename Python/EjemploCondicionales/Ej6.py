name = input("Ingrese su nombre: ")
gender = input("Ingrese su sexo (M/F): ")

if (gender == "F" and name < "M") or (gender == "M" and name > "N"):
    print("Usted pertenece al grupo A")
else:
    print("Usted pertenece al grupo B")
