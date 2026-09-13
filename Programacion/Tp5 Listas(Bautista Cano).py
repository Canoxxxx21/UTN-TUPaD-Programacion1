# Ejercicio 1: Múltiplos de 4
lista = [i for i in range(1, 101) if i % 4 == 0]
print(lista)
# Ejercicio 2: Mostrar el penúltimo elemento
lista2 = [1, 2, 3, 4, 5]
print(lista2[-2])
# Ejercicio 3: Agregar palabras a una lista
lista_vacia = []
lista_vacia.append("palabra1")
lista_vacia.append("palabra2")
lista_vacia.append("palabra3")
print(lista_vacia)
# Ejercicio 4: Modificar elementos de una lista
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)
# Ejercicio 5: Eliminar el número mayor
"El programa busca y elimina el valor máximo contenido en una lista de números y luego imprime por pantalla la lista resultante."
# Ejercicio 6: Mostrar los primeros valores
lista3 = [i for i in range(10, 31, 5)]
print(lista3[:2])
# Ejercicio 7: Cambiar los valores centrales
autos= ["sedan", "polo", "suran", "gol"]
autos[1] = "camion"
autos[2] = "camioneta"
print(autos)
# Ejercicio 8: Calcular números dobles
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)
# Ejercicio 9: Modificar una lista anidada
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# Agregar un producto al tercer cliente.
compras[2].append("jugo")
# Cambiar un producto del segundo cliente.
compras[1][1] = "tallarines"
# Eliminar un producto del primer cliente.
compras[0].remove("pan")
# Mostrar la lista modificada.
print(compras)  
# Ejercicio 10: Crear una lista anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)






