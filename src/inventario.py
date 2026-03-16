def menu():

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar un producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

inventario = []

def agregar_producto():
        nombre = input("Nombre del producto:\n")
        precio = float(input('Ingrese el precio: '))
        cantidad = int(input('Ingrese la cantidad: '))
        producto = {
            'Nombre': nombre,
            'Precio': precio,
            'Cantidad': cantidad
        }
        inventario.append(producto)

        print(f"Producto '{nombre}' agregado al inventario.\n")











while True:
    menu()

    try:
        opcion = int(input("Ingrese una opción\n"))
    except ValueError:
        print("Error: Por favor, ingrese un número válido.\n")

    if opcion == 1:
        agregar_producto()
        

    elif opcion == 2:
        print('INVENTARIO')
        print(inventario)
        print('')

    elif opcion == 3:
        print("Opcion no disponible aún\n")


    elif opcion == 4:
        print("Saliendo...")
        break