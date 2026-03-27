import time  # Importa el módulo time (sirve para pausas como sleep)
import servicios  # Importa tu archivo servicios.py donde están las funciones del inventario
from archivos import guardar_csv, cargar_csv  # Importa funciones para guardar y cargar CSV


inventario = []  # Crea una lista vacía que almacenará los productos


while True:  # Bucle infinito para que el programa se repita hasta que el usuario salga
    servicios.menu()  # Muestra el menú principal

    while True:  # Bucle para asegurar que la opción ingresada sea válida
        try:
            opcion = int(input("Ingrese una opción\n"))  # Pide una opción y la convierte a número
            break  # Si no hay error, sale del bucle
        except ValueError:  # Si el usuario escribe algo que no es número
            print("Error: Por favor, ingrese un número válido.")  # Muestra mensaje de error
            servicios.menu()  # Vuelve a mostrar el menú

    if opcion == 1:  # Si elige agregar producto
        while True:  # Bucle para validar nombre
            nombre = input("Nombre del producto: ")  # Pide el nombre
            if nombre == "":  # Verifica si está vacío
                print("Por favor ingrese un nombre")  # Mensaje de error
                continue  # Vuelve a pedir el nombre
            else:
                break  # Sale del bucle si es válido

        while True:  # Bucle para validar precio
            try:
                precio = float(input("Ingrese el precio: "))  # Convierte a número decimal
                break  # Sale si es válido
            except ValueError:
                print("Ingrese un valor numerico")  # Error si no es número

        while True:  # Bucle para validar cantidad
            try:
                cantidad = int(input("Ingrese la cantidad: "))  # Convierte a entero
                break  # Sale si es válido
            except ValueError:
                print("Ingrese un numero entero positivo")  # Error si no es entero

        servicios.agregar_producto(inventario, nombre, precio, cantidad)  
        # Llama a la función para agregar el producto

    elif opcion == 2:  # Mostrar inventario
        servicios.ver_inventario(inventario)  # Llama función que imprime los productos
        print("")  # Imprime una línea vacía

    elif opcion == 3:  # Buscar producto
        if len(inventario) == 0:  # Verifica si está vacío
            print("El inventario está vacío")  # Mensaje
        else:
            nombre_buscar = input("Nombre del producto: ")  # Pide nombre a buscar
            print(servicios.buscar_producto(inventario, nombre_buscar))  
            # Muestra el resultado de la búsqueda

    elif opcion == 4:  # Actualizar producto
        if len(inventario) == 0:  # Verifica si está vacío
            print("El inventario está vacío")  # Mensaje
        else:
            p_actualizar = input("Que producto desea actualizar: ")  # Pide nombre
            for p in inventario:  # Recorre cada producto
                if p["Nombre"].lower() == p_actualizar.lower():  
                    # Compara nombres ignorando mayúsculas
                    print("Producto encontrado. Ingrese los nuevos datos")  # Mensaje
                    N_nombre = input("Nuevo nombre: ")  # Nuevo nombre
                    N_precio = float(input("Nuevo precio: "))  # Nuevo precio
                    N_cantidad = int(input("Nueva cantidad: "))  # Nueva cantidad
                    servicios.actualizar_producto(p, N_nombre, N_precio, N_cantidad)  
                    # Llama función para actualizar
                    break
            else:
                print("Producto no encontrado")  
                    # Se ejecuta si ese producto del ciclo no coincide

    elif opcion == 5:  # Eliminar producto
        if len(inventario) == 0:  # Verifica si está vacío
            print("El inventario está vacío")  # Mensaje
        else:
            eliminar_p = input("Que producto desea eliminar: ")  # Pide nombre
            servicios.eliminar_producto(inventario, eliminar_p)  
            # Llama función para eliminar

    elif opcion == 6:  # Calcular estadísticas
        if len(inventario) == 0:  # Verifica si está vacío
            print("El inventario está vacío")  # Mensaje
        else:
            print(servicios.calcular_estadisticas(inventario))  
            # Muestra estadísticas

    elif opcion == 7:  # Guardar CSV
        ruta = input("Ingrese la ruta del archivo (ej: inventario.csv): ")  
        # Pide la ruta del archivo
        guardar_csv(inventario, ruta)  # Llama función para guardar

    elif opcion == 8:  # Cargar CSV
        ruta = input("Ingrese la ruta del archivo a cargar: ")  
        # Pide la ruta
        inventario = cargar_csv(ruta, inventario)  
        # Carga datos y reemplaza/mezcla inventario

    elif opcion == 9:  # Salir del programa
        print("Saliendo...")  # Mensaje
        time.sleep(1)  # Espera 1 segundo
        break  # Rompe el bucle principal y termina el programa

    else:  # Si la opción no es válida
        print("Ingresa una opcion del menú")  # Mensaje de error