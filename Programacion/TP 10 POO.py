

# ---------- Funciones auxiliares 
def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero.")


def pedir_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debe ingresar un número (ej: 7.5).")


# ============================================================
# EJERCICIO 1 - 
# ============================================================
class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila          # entero
        self.columna = columna    # entero
        self.valor = valor        # cadena


class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def existe(self, fila, columna):
        """Devuelve True si ya hay una celda en esa fila y columna."""
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return True
        return False

    def agregar(self, celda):
        self.celdasMatriz.append(celda)

    def mostrar(self):
        for celda in self.celdasMatriz:
            print("Fila:", celda.fila, "| Columna:", celda.columna, "| Valor:", celda.valor)

    def obtenerValor(self, fila, columna):
        """Retorna el valor de la celda o un mensaje si no existe."""
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"


def ejercicio1():
    matriz = Matriz()

    valor = input("Ingrese el valor de la celda (FIN para terminar): ")
    while valor != "FIN":
        fila = pedir_entero("Ingrese la fila: ")
        columna = pedir_entero("Ingrese la columna: ")

        if matriz.existe(fila, columna):
            print("Esa fila y columna ya fueron cargadas. No se agregó la celda.")
        else:
            matriz.agregar(Celda(fila, columna, valor))

        valor = input("Ingrese el valor de la celda (FIN para terminar): ")

    print("\n--- Valores cargados ---")
    matriz.mostrar()

    print("\n--- Consulta de una celda ---")
    f = pedir_entero("Fila a consultar: ")
    c = pedir_entero("Columna a consultar: ")
    print(matriz.obtenerValor(f, c))


# ============================================================
# EJERCICIO 2 
# ============================================================
class Nota:
    def __init__(self, catedra, notaExamen):
        self.catedra = catedra          # cadena
        self.notaExamen = notaExamen    # decimal


class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregarNota(self, nota):
        self.notas.append(nota)

    def calcularPromedio(self):
        if len(self.notas) == 0:
            return 0
        suma = 0
        for nota in self.notas:
            suma += nota.notaExamen
        return suma / len(self.notas)


def ejercicio2():
    alumnos = []
    salirAlumno = "NO"

    while salirAlumno != "SI":
        print("\nINGRESE DATOS DEL ALUMNO")
        nombre = input("INGRESE NOMBRE COMPLETO: ")
        legajo = pedir_entero("INGRESE LEGAJO: ")
        alumno = Alumno(nombre, legajo)

        salirNotas = "NO"
        while salirNotas != "SI":
            catedra = input("INGRESE NOMBRE CATEDRA: ")
            notaExamen = pedir_decimal("Nota: ")
            alumno.agregarNota(Nota(catedra, notaExamen))
            # Se carga una nota antes de preguntar, así siempre hay al menos 1
            salirNotas = input("DESEA SALIR DE LA CARGA DE NOTAS (SI/NO): ").upper()

        alumnos.append(alumno)
        salirAlumno = input("DESEA SALIR DE CARGA DE ALUMNOS (SI/NO): ").upper()

    print("\n========== DATOS CARGADOS ==========")
    for alumno in alumnos:
        print("\nAlumno:", alumno.nombreCompleto, "- Legajo:", alumno.legajo)
        for nota in alumno.notas:
            print("   Cátedra:", nota.catedra, "- Nota:", nota.notaExamen)
        print("El promedio del alumno es:", round(alumno.calcularPromedio(), 2))


# ============================================================
# EJERCICIO 3 
# ============================================================
class Ingrediente:
    def __init__(self, nombre, cantidad, unidadMedida):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidadMedida = unidadMedida


class Plato:
    def __init__(self, nombreCompleto, precio, esBebida):
        self.nombreCompleto = nombreCompleto
        self.precio = precio
        self.esBebida = esBebida
        self.ingredientes = []

    def agregarIngrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)


def ejercicio3():
    platosMenu = []
    otro = "SI"

    while otro == "SI":
        nombre = input("\nNombre del plato: ")
        precio = pedir_decimal("Precio: ")
        esBebida = (input("¿Es una bebida? (SI/NO): ").upper() == "SI")
        plato = Plato(nombre, precio, esBebida)

        if not esBebida:
            seguir = "SI"
            # Obligatorio al menos 1 ingrediente
            while seguir == "SI":
                nombreIng = input("  Nombre del ingrediente: ")
                cantidad = pedir_decimal("  Cantidad: ")
                unidad = input("  Unidad de medida (gramos, unidad, etc.): ")
                plato.agregarIngrediente(Ingrediente(nombreIng, cantidad, unidad))
                seguir = input("  ¿Agregar otro ingrediente? (SI/NO): ").upper()

        platosMenu.append(plato)
        otro = input("¿Desea cargar otro plato? (SI/NO): ").upper()

    print("\n-----------MENÚ----------------")
    for plato in platosMenu:
        print(plato.nombreCompleto)
        print("Precio: $", plato.precio)
        if not plato.esBebida:
            print("Ingredientes:")
            print("Nombre\tCantidad\tUnidad de Medida")
            for ing in plato.ingredientes:
                print(ing.nombre + "\t" + str(ing.cantidad) + "\t" + ing.unidadMedida)
        print("----------------------------------")


# ============================================================
# EJERCICIO 4 
# ============================================================
class ComponenteCPU:
    def __init__(self, componente, marca, cantidad, precio):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    def getSubtotal(self):
        return self.precio * self.cantidad


class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []

    def agregarComponente(self, componente):
        self.componentes.append(componente)

    def calcularCosto(self):
        total = 0
        for c in self.componentes:
            total += c.getSubtotal()
        return total

    def calcularPrecioVenta(self):
        costo = self.calcularCosto()
        if costo < 50000:
            ganancia = costo * 0.40
        else:
            ganancia = costo * 0.30
        return costo, ganancia, costo + ganancia


def ejercicio4():
    continuar = "SI"
    while continuar == "SI":
        marca = input("\nMarca de la computadora: ")
        modelo = input("Modelo: ")
        pc = Computadora(marca, modelo)

        otro = "SI"
        while otro == "SI":
            nombre = input("  Componente (ej: Memoria RAM 2Gb): ")
            marcaComp = input("  Marca del componente: ")
            cantidad = pedir_entero("  Cantidad: ")
            precio = pedir_decimal("  Precio por unidad: ")
            pc.agregarComponente(ComponenteCPU(nombre, marcaComp, cantidad, precio))
            otro = input("  ¿Agregar otro componente? (SI/NO): ").upper()

        costo, ganancia, venta = pc.calcularPrecioVenta()

        print("\n-----------Computadora----------------")
        print("Marca:", pc.marca)
        print("Modelo:", pc.modelo)
        print("Componentes:")
        print("Componente\tMarca\tCantidad\tPrecio x Unidad\tSubTotal")
        for c in pc.componentes:
            print(c.componente, "\t", c.marca, "\t", c.cantidad, "\t", c.precio, "\t", c.getSubtotal())
        print("Costo Total", costo)
        print("El precio sugerido de venta es", costo, "+", ganancia, "=", venta)

        continuar = input("\n¿Desea cotizar una nueva computadora? (SI/NO): ").upper()

    print("Fin de la cotización.")


# ============================================================
# EJERCICIO 5 
# ============================================================
class Habitacion:
    def __init__(self, nombre, metrosCuadrados):
        self.nombre = nombre
        self.metrosCuadrados = metrosCuadrados


class Vivienda:
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []

    def agregarHabitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        total = 0
        for h in self.habitaciones:
            total += h.metrosCuadrados
        if total > self.superficieTerreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")
        return total


class Barrio:
    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []

    def agregarVivienda(self, vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerreno(self):
        total = 0
        for v in self.viviendas:
            total += v.superficieTerreno
        return total

    def getSuperficieTotalTerrenoXManzana(self, manzana):
        total = 0
        for v in self.viviendas:
            if v.manzana == manzana:
                total += v.superficieTerreno
        return total

    def getSuperficieTotalCubierta(self):
        total = 0
        for v in self.viviendas:
            total += v.getMetrosCuadradosCubiertos()   # reutiliza el método de Vivienda
        return total


def ejercicio5():
    barrio = Barrio("Los Álamos", "Constructora Sur")

    v1 = Vivienda("San Martín", 123, "A", 1, 200)
    v1.agregarHabitacion(Habitacion("Dormitorio", 15))
    v1.agregarHabitacion(Habitacion("Cocina", 12))
    v1.agregarHabitacion(Habitacion("Baño", 6))

    v2 = Vivienda("San Martín", 125, "A", 2, 250)
    v2.agregarHabitacion(Habitacion("Dormitorio", 20))
    v2.agregarHabitacion(Habitacion("Living", 25))

    v3 = Vivienda("Belgrano", 456, "B", 1, 180)
    v3.agregarHabitacion(Habitacion("Dormitorio", 14))
    v3.agregarHabitacion(Habitacion("Cocina", 10))

    barrio.agregarVivienda(v1)
    barrio.agregarVivienda(v2)
    barrio.agregarVivienda(v3)

    print("Barrio:", barrio.nombre, "- Constructora:", barrio.empresaConstructora)
    print("Superficie total de terreno:", barrio.getSuperficieTotalTerreno(), "m2")
    print("Superficie de terreno manzana A:", barrio.getSuperficieTotalTerrenoXManzana("A"), "m2")
    print("Superficie de terreno manzana B:", barrio.getSuperficieTotalTerrenoXManzana("B"), "m2")
    print("Metros cubiertos vivienda 1:", v1.getMetrosCuadradosCubiertos(), "m2")
    print("Superficie total cubierta del barrio:", barrio.getSuperficieTotalCubierta(), "m2")

    # Prueba de la excepción: habitaciones más grandes que el terreno
    print("\nPrueba de excepción:")
    v4 = Vivienda("Mitre", 789, "B", 2, 30)
    v4.agregarHabitacion(Habitacion("Salón", 50))
    try:
        v4.getMetrosCuadradosCubiertos()
    except Exception as e:
        print("Error:", e)


# ============================================================
# MENÚ PRINCIPAL
# ============================================================
def main():
    opcion = ""
    while opcion != "0":
        print("\n===== TP POO EN PYTHON =====")
        print("1 - Celda y Matriz")
        print("2 - Alumnos y Notas")
        print("3 - Menú de Restaurant")
        print("4 - Costo de Computadora")
        print("5 - Barrio, Viviendas y Habitaciones")
        print("0 - Salir")
        opcion = input("Elija un ejercicio: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion != "0":
            print("Opción inválida.")


main()
