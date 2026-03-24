import time
import src.inventario


inventario = []


while True:
    src.inventario.menu()
    while True:
        try:
            opcion = int(input("Ingrese una opción\n"))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número válido.\n")
            src.inventario.menu()

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

        src.inventario.agregar_producto(nombre, precio, cantidad)
        

    elif opcion == 2:
        src.inventario.ver_inventario()
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
                    src.inventario.actualizar_producto(N_nombre, N_precio, N_cantidad)
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
                   src.inventario.eliminar_producto(producto)
                   print(f'Producto {producto['Nombre']} eliminado\n')
                   break
               else:
                   print(f'Producto {eliminar_p} no existe')
                 
                 
        
    elif opcion == 5:
        src.inventario.calcular_estadisticas()
        

    elif opcion == 6:
        print('Saliendo...')
        time.sleep(1)
        break
    
    else:
        print('Ingresa una opcion del menú\n')
