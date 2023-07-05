directorio = {}

def validacion_numero(telefono):
    if telefono.isnumeric() and len(telefono) == 10:
        return True
    return False


def formato_telefono(telefono):
    return telefono[:3] + "-" + telefono[3:6] + "-" + telefono[6:]

def nuevo_contacto():
    nombre = input("Introduce el nombre: ")
    telefono = input("Introduce el teléfono (10 dígitos): ")

    if validacion_numero(telefono):
        phone_format = formato_telefono(telefono)
        directorio[nombre] = phone_format
        print("Persona agregada correctamente a tu directorio.")
    else:
        print("El número de teléfono no es válido: ")

def buscar_telefono():
    nombre = input("Introduce el nombre de la persona: ")
    resultado = [nombre_completo + " " + telefono for nombre_completo, telefono in directorio.items() if nombre_completo.startswith(nombre)]

    if resultado:
        print("Resultados: ")
        for r in resultado:
            print(r)
    else:
        print("No se encontraron resultados con el nombre proporcionado.")

while True:
    print("----- Agenda Telefónica -----")
    print("1. Agregar persona")
    print("2. Buscar Teléfono")
    print("3. Salir")


    opcion = input("Elige una opción: ")

    if opcion == "1":
        nuevo_contacto
    elif opcion == "2":
        buscar_telefono
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, seleccione una de las opciones mencionadas")
