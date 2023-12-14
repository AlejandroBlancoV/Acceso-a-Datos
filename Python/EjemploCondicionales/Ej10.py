# Solicitar al usuario si quiere una pizza vegetariana o no
opcion = input("¿Desea una pizza vegetariana? (Sí/No): ")

# Verificar la opción del usuario y mostrar el menú de ingredientes disponibles
if opcion.lower() == "sí":
    print("Ingredientes disponibles para la pizza vegetariana:")
    print("1. Pimiento")
    print("2. Tofu")
else:
    print("Ingredientes disponibles para la pizza no vegetariana:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")

# Solicitar al usuario que elija un ingrediente
ingrediente_elegido = input("Seleccione un ingrediente (1-3): ")

# Verificar la opción del usuario y mostrar la pizza elegida y sus ingredientes
if opcion.lower() == "sí":
    pizza = "Pizza vegetariana"
    if ingrediente_elegido == "1":
        ingredientes = "Mozzarella, tomate, pimiento"
    elif ingrediente_elegido == "2":
        ingredientes = "Mozzarella, tomate, tofu"
else:
    pizza = "Pizza no vegetariana"
    if ingrediente_elegido == "1":
        ingredientes = "Mozzarella, tomate, peperoni"
    elif ingrediente_elegido == "2":
        ingredientes = "Mozzarella, tomate, jamón"
    elif ingrediente_elegido == "3":
        ingredientes = "Mozzarella, tomate, salmón"

# Mostrar la pizza elegida y sus ingredientes
print("La pizza elegida es:", pizza)
print("Ingredientes:", ingredientes)



