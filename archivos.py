import csv


def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print('El inventario está vacío')
        return
    try:
        with open(ruta, 'w', newline='') as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(['Nombre', 'Precio', 'Cantidad'])
            
            for producto in inventario:
                writer.writerow([
                    producto['Nombre'],
                    producto['Precio'],
                    producto['Cantidad']
                ])
        print(f'Invetario guardado en: {ruta}')
    except PermissionError:
        print("Error: No tienes permisos para escribir en esa ruta.")
    except Exception as e:
        print(f"Error inesperado al guardar: {e}")

def cargar_csv(ruta, inventario_actual):
    productos_cargados = []
    filas_invalidas = 0

    try:
        with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            encabezado = next(reader, None)
            if encabezado != ["Nombre", "Precio", "Cantidad"]:
                print("Error: Encabezado inválido. Debe ser: Nombre,Precio,Cantidad")
                return inventario_actual
                
            for fila in reader:
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    producto = {
                        "Nombre": nombre.strip(),
                        "Precio": precio,
                        "Cantidad": cantidad
                    }

                    productos_cargados.append(producto)

                except ValueError:
                    filas_invalidas += 1

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return inventario_actual
    except UnicodeDecodeError:
        print("Error: Problema de codificación en el archivo.")
        return inventario_actual
    except Exception as e:
        print(f"Error inesperado: {e}")
        return inventario_actual
        
    opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()

    if opcion == "S":
        inventario_actual = productos_cargados
        accion = "reemplazo"

    else:
        nombres_existentes = {p["Nombre"]: p for p in inventario_actual}

        for prod in productos_cargados:
            if prod["Nombre"] in nombres_existentes:
                existente = nombres_existentes[prod["Nombre"]]
                
                existente["Cantidad"] += prod["Cantidad"]

                if existente["Precio"] != prod["Precio"]:
                    existente["Precio"] = prod["Precio"]
            else:
                inventario_actual.append(prod)

        accion = "fusión (cantidad sumada y precio actualizado si cambia)"

    print("RESUMEN DE CARGA:")
    print(f"Productos cargados: {len(productos_cargados)}")
    print(f"Filas inválidas omitidas: {filas_invalidas}")
    print(f"Acción realizada: {accion}")

    return inventario_actual
    
