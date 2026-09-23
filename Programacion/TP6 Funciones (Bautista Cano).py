# Ejercicio 1: Hola Mundo

import math


def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()
# Ejercicio 2: Saludo personalizado

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))
# Ejercicio 3: Datos personales

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)
# Ejercicio 4: Área y perímetro del círculo

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")
# Ejercicio 5: Segundos a horas

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos son equivalentes a {segundos_a_horas(segundos)} horas.")
# Ejercicio 6: Tabla de multiplicar

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)
# Ejercicio 7: Operaciones básicas

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
# Ejercicio 8: Calcula el IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)
# Ejercicio 9: Conversión de temperatura

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)
# Ejercicio 10: Promedio de tres números

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return round(promedio, 2)
