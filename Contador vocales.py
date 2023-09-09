print ("Programa que cuenta las vocales de las palabras")
print ("================================================")
cadena = input("Ingrese una cadena de texto: ")

contador_vocales = 0

for caracter in cadena:
    if caracter in "aeiouAEIOU":
        contador_vocales += 1

print("El número de vocales es:", contador_vocales)
