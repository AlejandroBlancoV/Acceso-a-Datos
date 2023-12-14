'''Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por
ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de
teléfono con este formato y muestre por pantalla el número de teléfono sin el
prefijo y la extensión'''

telefono=input("Introduzca el teléfono con el formato prefijo-número-extension ")
posGuion=telefono.find('-')


#print(telefono[posGuion+1:posGuion+10])

posSegundoGuion=telefono[posGuion+1:len(telefono)].find('-')
posSegundoGuion+=posGuion
print(telefono[posGuion+1:posSegundoGuion+1])

arrayNum=telefono.split('-')
print(arrayNum[1])