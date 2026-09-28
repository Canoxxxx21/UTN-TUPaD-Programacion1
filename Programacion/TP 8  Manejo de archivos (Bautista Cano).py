import os


RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__), "productos.txt")
PRODUCTOS_INICIALES = [
	{"nombre": "Lapicera", "precio": 120.5, "cantidad": 30},
	{"nombre": "Cuaderno", "precio": 850.0, "cantidad": 15},
	{"nombre": "Regla", "precio": 300.0, "cantidad": 20},
]


def crear_archivo_inicial():
	try:
		with open(RUTA_ARCHIVO, "x", encoding="utf-8") as archivo:
			for producto in PRODUCTOS_INICIALES:
				archivo.write(
					f"{producto['nombre']},{producto['precio']:g},"
					f"{producto['cantidad']}\n"
				)
	except FileExistsError:
		pass


def cargar_productos():
	productos = []

	with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
		for linea in archivo:
			datos = linea.strip().split(",")
			if len(datos) != 3:
				print(f"Se omitió una línea con formato incorrecto: {linea.strip()}")
				continue

			nombre, precio, cantidad = datos
			try:
				productos.append(
					{
						"nombre": nombre,
						"precio": float(precio),
						"cantidad": int(cantidad),
					}
				)
			except ValueError:
				print(f"Se omitió una línea con datos inválidos: {linea.strip()}")

	return productos


def mostrar_productos(productos):
	if not productos:
		print("No hay productos cargados.")
		return

	for producto in productos:
		print(
			f"Producto: {producto['nombre']} | "
			f"Precio: ${producto['precio']:g} | "
			f"Cantidad: {producto['cantidad']}"
		)


def agregar_producto(productos):
	print("\nIngresá los datos del nuevo producto:")
	nombre = input("Nombre: ").strip()
	while not nombre or "," in nombre:
		print("El nombre no puede estar vacío ni contener comas.")
		nombre = input("Nombre: ").strip()

	while True:
		try:
			precio = float(input("Precio: "))
			if precio < 0:
				print("El precio no puede ser negativo.")
				continue
			break
		except ValueError:
			print("Ingresá un precio numérico, usando punto para los decimales.")

	while True:
		try:
			cantidad = int(input("Cantidad: "))
			if cantidad < 0:
				print("La cantidad no puede ser negativa.")
				continue
			break
		except ValueError:
			print("La cantidad debe ser un número entero.")

	productos.append(
		{"nombre": nombre, "precio": precio, "cantidad": cantidad}
	)
	with open(RUTA_ARCHIVO, "a", encoding="utf-8") as archivo:
		archivo.write(f"{nombre},{precio:g},{cantidad}\n")
	print("Producto agregado.")


def buscar_producto(productos):
	nombre_buscado = input("\nNombre del producto que querés buscar: ").strip()

	for producto in productos:
		if producto["nombre"].casefold() == nombre_buscado.casefold():
			print("Producto encontrado:")
			mostrar_productos([producto])
			return

	print(f"No se encontró el producto '{nombre_buscado}'.")


def guardar_productos(productos):
	with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
		for producto in productos:
			archivo.write(
				f"{producto['nombre']},{producto['precio']:g},"
				f"{producto['cantidad']}\n"
			)


def main():
	crear_archivo_inicial()

	try:
		productos = cargar_productos()
		print("Productos disponibles:")
		mostrar_productos(productos)

		agregar_producto(productos)
		buscar_producto(productos)

		guardar_productos(productos)
		print("\nLos cambios se guardaron en productos.txt.")
	except OSError as error:
		print(f"No se pudo acceder al archivo de productos: {error}")


if __name__ == "__main__":
	main()
