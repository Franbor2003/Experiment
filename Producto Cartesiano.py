print ("Programa que calcula el producto cartesiano")
print ("===========================================")
cadena_1 = input("Introduce la primera cadena de texto: ")
cadena_2 = input("Introduce la segunda cadena de texto: ")

for letra1 in cadena_1:
    for letra2 in cadena_2:
        print(letra1 + letra2, end=" ")
