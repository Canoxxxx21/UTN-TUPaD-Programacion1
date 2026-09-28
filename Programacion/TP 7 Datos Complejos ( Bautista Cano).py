# Ejercicio 1: Frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
# Ejercicio 2: Cambiar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800  
# Ejercicio 3: Lista de frutas
frutas = list(precios_frutas.keys())
# Ejercicio 5: Contar palabras
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
# Ejercicio 6: Notas de alumnos
Alumnos = {}
for i in range(3):
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} del alumno {nombre_alumno}: "))
        notas.append(nota)
    Alumnos[nombre_alumno] = tuple(notas)
    promedio = sum(Alumnos[nombre_alumno]) / len(Alumnos[nombre_alumno])
    print(f"El promedio de {nombre_alumno} es: {promedio}")
    # Ejercicio 7: Alumnos aprobados
    set_parcial1 = {101, 102, 103, 104, 105}
    set_parcial2 = {104, 105, 106, 107, 108}
    aprobados_ambos = set_parcial1.intersection(set_parcial2)
    aprobados_solo_uno = set_parcial1.symmetric_difference(set_parcial2)
    aprobados_al_menos_uno = set_parcial1.union(set_parcial2)
    # Ejercicio 8: Productos y stock
    stock_productos = {}
    while True:
        print("\nOpciones:")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades al stock de un producto existente")
        print("3. Agregar un nuevo producto")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            producto = input("Ingrese el nombre del producto a consultar: ")
            if producto in stock_productos:
                print(f"El stock de {producto} es: {stock_productos[producto]}")
            else:
                print(f"El producto {producto} no existe en el stock.")
        elif opcion == '2':
            producto = input("Ingrese el nombre del producto al que desea agregar unidades: ")
            if producto in stock_productos:
                unidades = int(input(f"Ingrese la cantidad de unidades a agregar al stock de {producto}: "))
                stock_productos[producto] += unidades
                print(f"Se han agregado {unidades} unidades al stock de {producto}. Nuevo stock: {stock_productos[producto]}")
            else:
                print(f"El producto {producto} no existe en el stock.")
        elif opcion == '3':
            producto = input("Ingrese el nombre del nuevo producto: ")
            if producto not in stock_productos:
                unidades = int(input(f"Ingrese la cantidad inicial de unidades para {producto}: "))
                stock_productos[producto] = unidades
                print(f"Se ha agregado el producto {producto} con un stock inicial de {unidades}.")
            else:
                print(f"El producto {producto} ya existe en el stock.")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-4).")
            # Ejercicio 9: Agenda
            agenda = {
                ('Lunes', '10:00'): 'Reunión de equipo',
                ('Martes', '14:00'): 'Cita con el cliente',
                ('Miércoles', '09:30'): 'Presentación del proyecto',
                ('Jueves', '16:00'): 'Llamada de seguimiento',
                ('Viernes', '11:00'): 'Revisión de informes'
            }
            # Consultar un evento
            dia = input("Ingrese el día: ")
            hora = input("Ingrese la hora (formato HH:MM): ")
            evento = agenda.get((dia, hora))
            if evento:
                print(f"El evento programado para {dia} a las {hora} es: {evento}")
            else:
                print(f"No hay eventos programados para {dia} a las {hora}.")
# Ejercicio 10: Países y capitales
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(capitales_paises)


    

