
inventario = []

producto = {"nombre": "Lapiz","precio": 500, "cantidad": 3}

while True:

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar un producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")


    opcion = int(input("Ingrese una opción\n"))

    if opcion == 1:
        nombre = input("Nombre del producto:\n")
        precio = float(input("Ingrese el precio:\n"))
        cantidad = int(input("Ingrese la cantidad:\n"))
        

        inventario.append(producto)

        print("Producto agregado exitosamente!!")

    elif opcion == 2:
        print(inventario)


    else:
        break

