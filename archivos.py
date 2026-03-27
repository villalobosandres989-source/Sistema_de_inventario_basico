import csv # Importa el módulo csv para trabajar con archivos tipo CSV


def guardar_csv(inventario, ruta, incluir_header=True): # Define la función para guardar datos en CSV
    if len(inventario) == 0: # Verifica si el inventario está vacío
        print("El inventario está vacío") # Muestra mensaje si no hay datos
        return # Termina la función
    
    try: # Inicia manejo de errores
        with open(ruta, "w", newline="", encoding='utf-8') as archivo: # Abre el archivo en modo escritura
            writer = csv.writer(archivo) # Crea un objeto para escribir en el CSV

            if incluir_header: # Verifica si se debe incluir encabezado
                writer.writerow(["Nombre", "Precio", "Cantidad"]) # Escribe la fila de títulos


            for producto in inventario: # Recorre cada producto del inventario

                writer.writerow( # Escribe una fila en el archivo
                    [producto["Nombre"], producto["Precio"], producto["Cantidad"]] # Datos del producto
                )
        print(f"Invetario guardado en: {ruta}") # Mensaje de éxito

    except PermissionError: # Error si no tienes permisos para escribir

        print("Error: No tienes permisos para escribir en esa ruta.") # Mensaje de error

    except Exception as e: # Captura cualquier otro error
        print(f"Error inesperado al guardar: {e}") # Muestra el error


def cargar_csv(ruta, inventario_actual): # Define función para cargar datos desde CSV
    productos_cargados = [] # Lista para guardar productos válidos
    filas_invalidas = 0 # Contador de filas con errores

    try: # Inicia manejo de errores
        with open(ruta, "r", newline="", encoding='utf-8') as archivo: # Abre el archivo en modo lectura
            reader = csv.reader(archivo) # Crea un lector de CSV

            encabezado = next(reader, None) # Lee la primera fila (encabezado)
            if encabezado != ["Nombre", "Precio", "Cantidad"]: # Verifica si el encabezado es correcto
                print("Error: Encabezado inválido. Debe ser: Nombre,Precio,Cantidad") # Mensaje de error
                return inventario_actual # Devuelve el inventario sin cambios

            for fila in reader: # Recorre cada fila del archivo
                if len(fila) != 3: # Verifica que la fila tenga 3 columnas
                    filas_invalidas += 1 # Cuenta la fila como inválida
                    continue # Salta a la siguiente fila

                nombre, precio, cantidad = fila # Asigna cada valor a una variable

                try: # Intenta convertir y validar datos
                    precio = float(precio) # Convierte precio a número decimal
                    cantidad = int(cantidad) # Convierte cantidad a entero

                    if precio < 0 or cantidad < 0: # Verifica que no sean negativos
                        raise ValueError # Lanza error si son inválidos

                    producto = { # Crea un diccionario con el producto
                        "Nombre": nombre.strip(), # Elimina espacios del nombre
                        "Precio": precio, # Guarda el precio
                        "Cantidad": cantidad, # Guarda la cantidad
                    }

                    productos_cargados.append(producto)  # Agrega el producto a la lista

                except ValueError:  # Si hay error en conversión o validación
                    filas_invalidas += 1  # Cuenta la fila como inválida

    except FileNotFoundError:  # Si el archivo no existe
        print("Error: Archivo no encontrado.")  # Mensaje de error
        return inventario_actual  # Devuelve inventario original

    except UnicodeDecodeError:  # Si hay error de codificación
        print("Error: Problema de codificación en el archivo.")  # Mensaje
        return inventario_actual  # Devuelve inventario original

    except Exception as e:  # Cualquier otro error
        print(f"Error inesperado: {e}")  # Muestra error
        return inventario_actual  # Devuelve inventario original

    opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()  # Pide decisión al usuario

    if opcion == "S":  # Si el usuario quiere reemplazar
        inventario_actual = productos_cargados  # Sustituye todo el inventario
        accion = "reemplazo"  # Guarda tipo de acción

    else:  # Si el usuario quiere fusionar
        nombres_existentes = {p["Nombre"]: p for p in inventario_actual}  # Crea diccionario para búsqueda rápida

        for prod in productos_cargados:  # Recorre productos cargados
            if prod["Nombre"] in nombres_existentes:  # Si el producto ya existe
                existente = nombres_existentes[prod["Nombre"]]  # Obtiene el producto existente

                existente["Cantidad"] += prod["Cantidad"]  # Suma la cantidad

                if existente["Precio"] != prod["Precio"]:  # Si el precio es diferente
                    existente["Precio"] = prod["Precio"]  # Actualiza el precio

            else:  # Si el producto no existe
                inventario_actual.append(prod)  # Lo agrega al inventario

        accion = "fusión (cantidad sumada y precio actualizado si cambia)"  # Describe la acción

    print("RESUMEN DE CARGA:")  # Título del resumen
    print(f"Productos cargados: {len(productos_cargados)}")  # Muestra cantidad de productos válidos
    print(f"Filas inválidas omitidas: {filas_invalidas}")  # Muestra errores
    print(f"Acción realizada: {accion}")  # Muestra qué se hizo

    return inventario_actual  # Devuelve el inventario actualizado
