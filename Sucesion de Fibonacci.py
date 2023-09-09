print ("Programa que imprime a los 100 primeros números de la sucesión de Fibonacci")
print ("===========================================================================")
a, b = 0, 1

print(a)
print(b)

for i in range(98):
    c = a + b
    a, b = b, c
    print(c)
