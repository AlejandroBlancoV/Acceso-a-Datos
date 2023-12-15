import random


numeroRandom = random.randint(1, 10)
print("Juego de adivinar el numero entre el 1 y el 10:")
print("Tienes 3 intentos")
for i in range(1, 4):
    numero = int(input("Introduce un numero: "))
    if numero == numeroRandom:
        print("Has acertado!")
        break

    elif numero > numeroRandom:
        print("Has fallado!")
        print("Te quedan "+str(3-i)+" intentos")
        print("El numero a adivinar es menor")
        if i == 3:
            print("Se acabaron tus intentos, el numero era "+str(numeroRandom))
            break
    
    else :
        print("Has fallado!")
        print("Te quedan "+str(3-i)+" intentos")
        print("El numero a adivinar es mayor")
        if i == 3:
            print("Se acabaron tus intentos, el numero era "+str(numeroRandom))
            break

  
        
