# Ejercicio 5: adivinar un número aleatorio entre 0 y 9.
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
        break
    else:
        print("Número incorrecto. Intenta de nuevo.")
        