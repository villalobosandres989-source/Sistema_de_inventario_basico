while True:

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar un producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese una opción\n"))
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

    if opcion == 1:
        nombre = input("Nombre del producto:\n")
        precio = float(input("Ingrese el precio:\n"))
        cantidad = int(input("Ingrese la cantidad:\n"))
        print(f"Producto '{nombre}' agregado al inventario.")

    elif opcion == 2:
        print("Opcion no disponible aún")

    elif opcion == 3:
        print("Opcion no disponible aún")


    elif opcion == 4:
        print("Saliendo...")
        break
