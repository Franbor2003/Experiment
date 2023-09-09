print("Programa para seleccionar a aptos de donar sangre")
print ("=================================================")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso en kg: "))
pulso = int(input("Ingrese su pulso en latidos por minuto: "))
plaquetas = int(input("Ingrese su conteo de plaquetas por microlitro de sangre: "))

if edad >= 18 and edad <= 65 and peso >= 50 and pulso >= 50 and pulso <= 100 and plaquetas >= 150000:
    print("Apto para donar sangre")
else:
    print("No apto para donar sangre")
