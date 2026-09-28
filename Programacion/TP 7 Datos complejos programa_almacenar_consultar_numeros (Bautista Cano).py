#Ejercicio 4 : Escribí un programa que permita almacenar y consultar números telefónicos.  Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.• Luego, pedí un nombre y mostrale el número asociado, si existe
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono del contacto: ")
    contactos[nombre] = numero

nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ")
if nombre_consulta in contactos:
    print(f"El número de teléfono de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"El contacto {nombre_consulta} no existe.")