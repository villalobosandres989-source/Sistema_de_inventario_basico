import time
def menu():

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar un producto")
    print("2. Mostrar inventario")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")


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
            print(f'Nombre: {i['Nombre']} | Precio: {i['Precio']:.3f} | Cantidad: {i['Cantidad']}')



def actualizar_producto():
    nombre_buscar = input("¿Cuál producto desea actualizar?\n")
    for producto in inventario:
        if producto['Nombre'].lower() == nombre_buscar.lower():
            print("Producto encontrado. Ingrese los nuevos datos.\n")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_precio = float(input("Nuevo precio: "))
            nueva_cantidad = int(input("Nueva cantidad: "))

            producto['Nombre'] = nuevo_nombre
            producto['Precio'] = nuevo_precio
            producto['Cantidad'] = nueva_cantidad

            print("Producto actualizado correctamente.\n")
            return
        
    print("Producto no encontrado.\n")


def eliminar_producto():

    nombre_buscar = input("Ingrese el nombre del producto que desea eliminar:\n")

    for producto in inventario:

        if producto['Nombre'].lower() == nombre_buscar.lower():

            inventario.remove(producto)

            print("Producto eliminado correctamente.\n")
            return

    print("Producto no encontrado.\n")






















while True:
    menu()

    try:
        opcion = int(input("Ingrese una opción\n"))
    except ValueError:
        print("Error: Por favor, ingrese un número válido.\n")

    if opcion == 1:
        nombre = input("Nombre del producto:\n")
        precio = float(input('Ingrese el precio: '))
        cantidad = int(input('Ingrese la cantidad: '))

        agregar_producto(nombre, precio, cantidad)
        

    elif opcion == 2:
        ver_inventario()
        print('')

    elif opcion == 3:
        actualizar_producto()


    elif opcion == 4:
        eliminar_producto()

    elif opcion == 5:
        print('Saliendo...')
        time.sleep(1)
        break


    
       
    