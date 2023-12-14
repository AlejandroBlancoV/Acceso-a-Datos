email=input("Introduzca su email ")
arrayEmail=email.split('@')
nuevoDominio="cebem.es"
nuevoEmail=arrayEmail[0]+"@"+nuevoDominio
print("NUEVO EMAIL "+nuevoEmail)