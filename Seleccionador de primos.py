print ("Programa que determina si un numero es primo o no")
print ("=================================================")
numero = int(input("Ingrese un número: "))

contador_divisores = 0

for divisor in range(1, int(numero**0.5)+1):
    if numero % divisor == 0:
        contador_divisores += 1

if contador_divisores == 1:
    print("Es un número primo")
else:
    print("No es un número primo")
