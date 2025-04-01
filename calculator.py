import random

import math

print("Bienvendio a la calculadora aleatoria\n")
r1 = random.randint(10, 100)
print(f"El numero aleatorio para la operacion es: {r1}")

print("Raiz")
print("Cuadrado")
print("Ambos")


opcion =  input("Introduzca la opcion que desea operar con el numero aleatorio:\n").lower()

if opcion == "raiz":
    print(f"La raiz cuadrada con el numero aleatorio es {math.sqrt(r1):.2}")
elif opcion == "cuadrado":
    print(f"El cuadrado del numero aleatorio es: {math.pow(r1, r1):.2}")
elif opcion == "ambos":
    print(f"La raiz del numero aleatorio es: {math.sqrt(r1):.2} y el cuadrado es: {math.pow(r1, r1):.2}")
else:
    print("Opcion no valida.")