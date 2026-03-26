import time
import servicios
from archivos import guardar_csv, cargar_csv


inventario = []


while True:
    servicios.menu()
    while True:
        try:
            opcion = int(input("Ingrese una opción\n"))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
            servicios.menu()

    if opcion == 1:
        while True:
            nombre = input("Nombre del producto: ")
            if nombre == '':
                print('Por favor ingrese un nombre')
                continue
            else:
                break
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

        servicios.agregar_producto(inventario,nombre, precio, cantidad)
        

    elif opcion == 2:
        servicios.ver_inventario(inventario)
        print('')
        
    elif opcion == 3:
        if len(inventario) == 0:
            print('El inventario está vacío')
        else:
            nombre_buscar = input('Nombre del producto: ')
            print(servicios.buscar_producto(inventario, nombre_buscar))

    elif opcion == 4:
        if len(inventario) == 0:
            print('El inventario está vacío')
        else:
            p_actualizar = input('Que producto desea actualizar: ')
            for p in inventario:
                if p['Nombre'].lower() == p_actualizar.lower():
                    print('Producto encontrado. Ingrese los nuevos datos')
                    N_nombre = input('Nuevo nombre: ')
                    N_precio = float(input('Nuevo precio: '))
                    N_cantidad = int(input('Nueva cantidad: '))
                    servicios.actualizar_producto(p,N_nombre, N_precio, N_cantidad)
                else:
                    print('Producto no encontrado')
                    
                    
    elif opcion == 5:
        if len(inventario) == 0:
            print('El inventario está vacío')
        else:
            eliminar_p = input('Que producto desea eliminar: ')
            servicios.eliminar_producto(inventario, eliminar_p)
    
    elif opcion == 6:
        if len(inventario) == 0:
            print('El inventario está vacío')
        else:
            print(servicios.calcular_estadisticas(inventario))


    elif opcion == 7:
        ruta = input("Ingrese la ruta del archivo (ej: inventario.csv): ")
        guardar_csv(inventario, ruta)

    elif opcion == 8:
        ruta = input("Ingrese la ruta del archivo a cargar: ")
        inventario = cargar_csv(ruta, inventario)
    

    elif opcion == 9:
        print('Saliendo...')
        time.sleep(1)
        break
    
    else:
        print('Ingresa una opcion del menú')
