import json

asientos_iniciales = [
    ["\n"],
    ["01", "02", "03", " ", " ", "04", "05", "06", "\n"],
    ["07", "08", "09", " ", " ", "10", "11", "12", "\n"],
    ["13", "14", "15", " ", " ", "16", "17", "18", "\n"],
    ["19", "20", "21", " ", " ", "22", "23", "24", "\n"],
    ["25", "26", "27", " ", " ", "28", "29", "30", "\n"],
    ["31", "32", "33", " ", " ", "34", "35", "36", "\n"],
    ["37", "38", "39", " ", " ", "40", "41", "42", "\n"]
]

asientos = [
    ["\n"],
    ["01", "02", "03", " ", " ", "04", "05", "06", "\n"],
    ["07", "08", "09", " ", " ", "10", "11", "12", "\n"],
    ["13", "14", "15", " ", " ", "16", "17", "18", "\n"],
    ["19", "20", "21", " ", " ", "22", "23", "24", "\n"],
    ["25", "26", "27", " ", " ", "28", "29", "30", "\n"],
    ["31", "32", "33", " ", " ", "34", "35", "36", "\n"],
    ["37", "38", "39", " ", " ", "40", "41", "42", "\n"]
]

pasajeros = {}

# Función para guardar los datos en un archivo JSON
def guardar_datos():
    with open('datos_pasajeros.json', 'w') as file:
        json.dump(pasajeros, file, indent=4)
    print("Datos guardados en datos_pasajeros.json")

# Función asientos disponibles
def ver_asientos():
    print("Asientos disponibles:")
    for fila in asientos:
        for asiento in fila:
            if asiento in pasajeros:
                print("X", end=" ")
            else:
                print(asiento, end=" ")
        print()

# Función para comprar un asiento
def comprar_asiento():
    nombre = input("Ingrese nombre del pasajero: ")
    rut = input("Ingrese RUT del pasajero (sin guión ni puntos): ")
    telefono = input("Ingrese teléfono del pasajero: ")
    codigo_descuento = input("Ingrese código descuento (si tiene): ")

    if not rut.isdigit() or len(rut) != 9:
        print("RUT inválido. Debe tener 9 dígitos y no contener guiones ni puntos.")
        return

    if not telefono.isdigit() or not (900000000 <= int(telefono) <= 999999999):
        print("Teléfono inválido. Debe ser un número entre 900000000 y 999999999.")
        return

    ver_asientos()  # Mostrar asientos disponibles
    try:
        asiento = int(input("Seleccione el número del asiento que desea comprar: "))
    except ValueError:
        print("Número de asiento inválido. Debe ser un número.")
        return

    if str(asiento) in pasajeros:
        print("El asiento no está disponible, Por favor elija otro asiento.")
        return

    if asiento >= 31:
        precio = 240000
    else:               # Calcular precio base
        precio = 78900     
    if codigo_descuento.lower() == "bancoduoc":
        precio *= 0.85  # Aplicar descuento si hay código válido

    print("El valor del pasaje es: ", precio)

    confirmar = input("¿Desea confirmar la compra? (si/no): ")

    if confirmar.lower() == "si":
        pasajeros[str(asiento)] = {
            "nombre": nombre,
            "rut": rut,
            "telefono": telefono,
            "codigo": codigo_descuento,
            "precio": precio,
        }

        # Marcar asiento como ocupado con "X"
        for fila in asientos:
            for i in range(len(fila)):
                if fila[i] == str(asiento):
                    fila[i] = "X"

        print("Compra realizada con éxito.")
        guardar_datos()  # Guardar datos en el archivo JSON
    else:
        print("Compra Cancelada.")

# Función para anular un vuelo
def anular_vuelo():
    ver_asientos()  # Mostrar asientos disponibles
    try:
        asiento = int(input("Seleccione el número de asiento que desea anular: "))
    except ValueError:
        print("Número de asiento inválido. Debe ser un número.")
        return

    if str(asiento) in pasajeros:
        del pasajeros[str(asiento)]  # Eliminar datos del pasajero

        # Reemplazar "X" por número de asiento en el mapa
        for fila_inicial, fila_actual in zip(asientos_iniciales, asientos):
            for i in range(len(fila_actual)):
                if fila_actual[i] == "X" and fila_inicial[i] == str(asiento):
                    fila_actual[i] = str(asiento)

        print("El pasaje ha sido anulado.")
        guardar_datos()  # Guardar datos en el archivo JSON
    else:
        print("El asiento no está ocupado")

# Función para modificar datos
def modificar_datos():
    ver_asientos()
    try:
        asiento = int(input("Seleccione el número de asiento del pasajero: "))
    except ValueError:
        print("Número de asiento inválido. Debe ser un número.")
        return

    if str(asiento) in pasajeros:
        rut = input("Ingrese RUT del pasajero para verificar: ")
        if pasajeros[str(asiento)]["rut"] == rut:
            print("Datos actuales del pasajero: ")
            print(pasajeros[str(asiento)])
            print("1. Modificar Nombre")
            print("2. Modificar Teléfono")
            try:
                opcion = int(input("Seleccione la opción que desea modificar: "))
                if opcion == 1:
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    pasajeros[str(asiento)]["nombre"] = nuevo_nombre
                    print("Nombre modificado con éxito.")
                elif opcion == 2:
                    nuevo_telefono = input("Ingrese nuevo teléfono: ")
                    if not nuevo_telefono.isdigit() or not (900000000 <= int(nuevo_telefono) <= 999999999):
                        print("Teléfono inválido. Debe ser un número entre 900000000 y 999999999.")
                        return
                    pasajeros[str(asiento)]["telefono"] = nuevo_telefono
                    print("Teléfono modificado con éxito")
                else:
                    print("Opción no válida")
            except ValueError:
                print("Opción debe ser un número entre 1 y 2.")
            guardar_datos()  # Guardar datos en el archivo JSON
        else:
            print("RUT no coincide con el pasajero del asiento seleccionado.")
    else:
        print("El asiento no está ocupado")

# Función para el menú
def menu():
    while True:
        print("\n Menú")
        print("1. Ver asientos disponibles")
        print("2. Comprar asiento")
        print("3. Anular vuelo")
        print("4. Modificar datos de pasajero")
        print("5. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                ver_asientos()
            elif opcion == 2:
                comprar_asiento()
            elif opcion == 3:
                anular_vuelo()
            elif opcion == 4:
                modificar_datos()
            elif opcion == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Debe ser entre 1 y 5.")
        except ValueError:
            print("Opción debe ser un número entre 1 y 5. Intente nuevamente.")

menu()
