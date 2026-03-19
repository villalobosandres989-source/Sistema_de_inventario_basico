import time
def menu():

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar un producto")
    print("2. Mostrar inventario")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Calcular estadísticas")
    print("6. Salir")


inventario = []

def agregar_producto(nombre, precio, cantidad):
        
        producto = {
            'Nombre': nombre,
            'Precio': precio,
            'Cantidad': cantidad
        }
        inventario.append(producto)

        print(f"Producto '{nombre}' agregado al inventario.\n")

def ver_inventario():
    if len(inventario) == 0:
        print('El inventario está vacío')
    else:
        for i in inventario:
            print(f'Nombre: {i['Nombre']} | Precio: {i['Precio']}$ | Cantidad: {i['Cantidad']}')

def actualizar_producto(nombre_buscar, nuevo_nombre, nuevo_precio, nueva_cantidad):
    for producto in inventario:
        if producto['Nombre'].lower() == nombre_buscar.lower():
            print("Producto encontrado. Ingrese los nuevos datos.\n")

            producto['Nombre'] = nuevo_nombre
            producto['Precio'] = nuevo_precio
            producto['Cantidad'] = nueva_cantidad
            print("Producto actualizado correctamente.\n")
            return True
    return False
        
def eliminar_producto(nombre_buscar):
    

    for producto in inventario:

        if producto['Nombre'].lower() == nombre_buscar.lower():

            inventario.remove(producto)

            print("Producto eliminado correctamente.\n")
            

    print("Producto no encontrado.\n")
    
def calcular_estadisticas():
    contar = len(inventario)
    total = sum(productos['Precio'] * productos['Cantidad'] for productos in inventario)
    print(f'La cantidad total de productos es: {contar}')
    print(f'El valor total del inventario es: {total}$')
    print('')
    

while True:
    menu()
    while True:
        try:
            opcion = int(input("Ingrese una opción\n"))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número válido.\n")
            menu()

    if opcion == 1:
        nombre = input("Nombre del producto: ")
        while True:
            try:

                precio = float(input('Ingrese el precio: '))
                break
            except ValueError:
                print('Ingrese un valor numerico')
        while True:
            try:

                cantidad = int(input('Ingrese la cantidad: '))
                break
            except ValueError:
                print('Ingrese un numero entero positivo')

        agregar_producto(nombre, precio, cantidad)
        

    elif opcion == 2:
        ver_inventario()
        print('')

    elif opcion == 3:
        
        if len(inventario) ==0:
            print('El inventario está vacío\n')
            continue
        cancelar = False
        while True:
            nombre_buscar = input("¿Cuál producto desea actualizar?\n")
            existe = any(producto['Nombre'].lower() == nombre_buscar.lower() for producto in inventario)

            if existe:
                break
            else:
                print('Producto no encontrado')
                opcion_reintentar = input('Desea intentar de nuevo? (si/no): ').lower()

                if opcion_reintentar == 'no':
                    print('\nInventaro actual:')
                    ver_inventario()
                    print('')
                    cancelar = True
                    break
                elif opcion_reintentar != 'si':
                    print('opción inválida')
        if cancelar:
            continue
        nuevo_nombre = input('Nuevo nombre: ')

        while True:
            try:
                nuevo_precio = float(input('Nuevo Precio: '))
                if nuevo_precio < 0:
                    print('Ingrese un numero positivo')
                else:
                    break
            except ValueError:
                print('Ingrese un valor numérico')
        while True:
            try:
                nueva_cantidad = int(input('Nueva Cantidad: '))
                if nueva_cantidad < 0:
                    print('Ingrese un número positivo')
                else:
                    break
            except ValueError:
                print('Ingrese un número entero positivo')         
            
        actualizar_producto(nombre_buscar, nuevo_nombre, nuevo_precio, nueva_cantidad)


    elif opcion == 4:
        cancelar = False
        while True:
            nombre_buscar = input('Que producto desea eliminar:\n')

            existe = any(producto['Nombre'].lower() == nombre_buscar.lower() for producto in inventario)

            if existe:
                eliminar_producto(nombre_buscar)
                break
            else:
                print('Producto no encontrado')

                opcion_reintentar = input('Volver a intentar? (si/no): ').lower()

                if opcion_reintentar == 'no':
                    print('\nInventario actual:')
                    ver_inventario()
                    print('')
                    cancelar == True
                    break
                elif opcion_reintentar != 'si':
                    print('Opcion Inválida.\n')
        if cancelar:
            continue
        
        
    elif opcion == 5:
        calcular_estadisticas()
        

    elif opcion == 6:
        print('Saliendo...')
        time.sleep(1)
        break
    
    else:
        print('Ingresa una opcion del menú\n')

