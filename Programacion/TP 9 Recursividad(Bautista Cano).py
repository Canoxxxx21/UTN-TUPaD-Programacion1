# Ejercicio 1: Factorial
# Calcula el factorial de un número.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejercicio 2: Fibonacci
# Calcula la serie de Fibonacci.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejercicio 3: Potencia
# Calcula una potencia usando recursión.
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Ejercicio 4: Decimal a binario
# Pasa un número decimal a binario con recursión.
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Ejercicio 5: Palíndromo
# Comprueba si una palabra se lee igual al derecho y al revés.
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# Ejercicio 6: Suma de dígitos
# Suma los dígitos de un número sin convertirlo a texto.
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

# Ejercicio 7: Bloques de la pirámide
# Suma los bloques de todos los niveles.
def contar_bloques(n):
    if n <= 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

# Ejercicio 8: Contar un dígito
# Cuenta cuántas veces aparece un dígito en un número.
def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
   