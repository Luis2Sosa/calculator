# Importamos los módulos
import random
import math

# Damos la bienvenida al usuario
print("Bienvendio a la calculadora aleatoria\n")

# Un numero aleatorio del 10 al 100
r1 = random.randint(10, 100)
print(f"El numero aleatorio para la operacion es: {r1}\n")


print("Raiz")
print("Cuadrado")
print("Ambos")

# Pedimos al usuario que introduzca una opción de la que hay disponible
opcion =  input("Introduzca la opcion de la anteriores que desea operar con el numero aleatorio:\n").lower()

# Usamos las condiciones para cada caso
if opcion == "raiz":
    print(f"La raiz cuadrada con el numero aleatorio es {math.sqrt(r1):.2}")
elif opcion == "cuadrado":
    print(f"El cuadrado del numero aleatorio es: {math.pow(r1, r1):.2}")
elif opcion == "ambos":
    print(f"La raiz del numero aleatorio es: {math.sqrt(r1):.2} y el cuadrado es: {math.pow(r1, r1):.2}")
else:
    print("Opcion no valida.")
    
# Comentario de prueba para git .