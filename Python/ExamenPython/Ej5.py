while True:
    entrada = input("No me iré hasta que me digas la palabra mágica:")
    if entrada.lower() == "salir":
        print("Menos mal, ya estaba algo cansado de repetir tus textos, a que no era tan difícil?")
        break
    print(entrada)
