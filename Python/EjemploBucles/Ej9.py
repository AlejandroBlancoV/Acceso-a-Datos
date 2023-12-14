# Almacenar la contraseña en una variable
contraseña = "contraseña"

# Pedir al usuario que introduzca la contraseña
while True:
    input_contraseña = input("Introduce la contraseña: ")

    # Comprobar si la contraseña es correcta
    if input_contraseña == contraseña:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
