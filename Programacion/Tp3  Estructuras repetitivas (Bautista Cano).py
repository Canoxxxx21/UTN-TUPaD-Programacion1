# Ejercicio 1: imprimir los números enteros del 0 al 100, uno por línea.
for i in range(101):
    print(i)

# Ejercicio 2: contar los dígitos de un número entero.
numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

# Ejercicio 3: sumar los números entre dos valores, sin incluirlos.
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
suma = 0
if valor1 < valor2:
    menor = valor1
    mayor = valor2
else:
    menor = valor2
    mayor = valor1
for i in range(menor + 1, mayor):
    suma += i
print(f"La suma de los números entre {valor1} y {valor2} es: {suma}")

# Ejercicio 4: sumar números hasta que el usuario ingrese 0.
total = 0
while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print(f"El total acumulado es: {total}")

# Ejercicio 5: el juego se encuentra en "Juego Tp3 (Bautista Cano).py".

# Ejercicio 6: imprimir los números pares del 100 al 0, en orden decreciente.
for i in range(100, -1, -2):
    print(i)

# Ejercicio 7: sumar los números desde 0 hasta un entero positivo.
numero = int(input("Ingrese un número entero positivo: "))
while numero <= 0:
    numero = int(input("El número debe ser mayor que 0. Intente nuevamente: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(f"La suma de los números entre 0 y {numero} es: {suma}")

# Ejercicio 8: contar pares, impares, negativos y positivos.
cantidad_numeros = 100
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1
print(f"El número de pares es: {pares}")
print(f"El número de impares es: {impares}")
print(f"El número de negativos es: {negativos}")
print(f"El número de positivos es: {positivos}")

# Ejercicio 9: calcular la media de 100 números enteros.
media = 0
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    media += numero
media /= cantidad_numeros
print(f"La media de los números ingresados es: {media}")

# Ejercicio 10: invertir el orden de los dígitos de un número entero.
numero = int(input("Ingrese un número entero: "))
signo = 1
if numero < 0:
    signo = -1
    numero = numero * -1
numero_invertido = 0
while numero > 0:
    numero_invertido = numero_invertido * 10 + numero % 10
    numero //= 10
numero_invertido *= signo
print(f"El número invertido es: {numero_invertido}")