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
            print(f'Nombre: {i['Nombre']} | Precio: {i['Precio']}$ | Cantidad: {i['Cantidad']} unidades')

def actualizar_producto(p, N_nombre, N_precio, N_cantidad):
        p['Nombre'] = N_nombre
        p['Precio'] = N_precio
        p['Cantidad'] = N_cantidad
        print("Producto actualizado correctamente.\n")
        
        
def eliminar_producto(eliminar_p):
    inventario.remove(eliminar_p)
    
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
        if len(inventario) == 0:
            print('El inventario está vacío\n')
        else:
            p_actualizar = input('Que producto desea actualizar: ')
            for p in inventario:
                if p['Nombre'].lower() == p_actualizar.lower():
                    print('Producto encontrado. Ingrese los nuevos datos')
                    N_nombre = input('Nuevo nombre: ')
                    N_precio = float(input('Nuevo precio: '))
                    N_cantidad = int(input('Nueva cantidad: '))
                    actualizar_producto(p, N_nombre, N_precio, N_cantidad)
                else:
                    print('Producto no encontrado\n')
                    
                    
    elif opcion == 4:
        if len(inventario) == 0:
            print('El inventario está vacío\n')
        else:
             eliminar_p = input('Que producto desea eliminar: ')
             
             for producto in inventario:
               if producto['Nombre'].lower() == eliminar_p.lower():
                   print('Producto encontrado')
                   eliminar_producto(producto)
                   print(f'Producto {producto['Nombre']} eliminado\n')
                   break
               else:
                   print(f'Producto {eliminar_p} no existe')
                 
                 
        
    elif opcion == 5:
        calcular_estadisticas()
        

    elif opcion == 6:
        print('Saliendo...')
        time.sleep(1)
        break
    
    else:
        print('Ingresa una opcion del menú\n')

