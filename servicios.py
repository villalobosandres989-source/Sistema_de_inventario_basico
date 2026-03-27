def menu():  # Define la función del menú principal

    print("\n=== MENU PRINCIPAL ===")  # Imprime un salto de línea y el título del menú
    print("1. Agregar un producto")  # Muestra la opción 1
    print("2. Mostrar inventario")  # Muestra la opción 2
    print("3. Buscar producto")  # Muestra la opción 3
    print("4. Actualizar producto")  # Muestra la opción 4
    print("5. Eliminar producto")  # Muestra la opción 5
    print("6. Calcular estadísticas")  # Muestra la opción 6
    print("7. Guardar CSV")  # Muestra la opción 7
    print("8. Cargar CSV")  # Muestra la opción 8
    print("9. Salir")  # Muestra la opción 9



def agregar_producto(inventario,nombre, precio, cantidad):  # Función para agregar un producto al inventario
        
        producto = {  # Crea un diccionario con los datos del producto
            'Nombre': nombre,  # Guarda el nombre del producto
            'Precio': precio,  # Guarda el precio del producto
            'Cantidad': cantidad  # Guarda la cantidad disponible
        }
        inventario.append(producto)  # Agrega el producto a la lista inventario

        print(f"Producto '{nombre}' agregado al inventario.")  # Muestra mensaje de confirmación


def ver_inventario(inventario):  # Función para mostrar todos los productos
    if len(inventario) == 0:  # Verifica si el inventario está vacío
        print('El inventario está vacío')  # Muestra mensaje si no hay productos
    else:
        for i in inventario:  # Recorre cada producto en la lista
            print(f'Nombre: {i['Nombre']} | Precio: {i['Precio']}$ | Cantidad: {i['Cantidad']} unidades')
            # Imprime los datos del producto (nombre, precio y cantidad)
            
            
            
def buscar_producto(inventario, nombre):  # Función para buscar un producto por nombre
    for producto in inventario:  # Recorre cada producto en el inventario
                if producto['Nombre'].lower() == nombre.lower():  # Compara nombres ignorando mayúsculas/minúsculas
                    return producto  # Si lo encuentra, devuelve el producto
    print('Producto no encontrado')  # Si no lo encuentra, muestra mensaje
    return None  # Devuelve None si no existe

def actualizar_producto(inventario, N_nombre, N_precio, N_cantidad):  # Función para actualizar un producto
        inventario['Nombre'] = N_nombre  # Cambia el nombre del producto
        inventario['Precio'] = N_precio  # Cambia el precio del producto
        inventario['Cantidad'] = N_cantidad  # Cambia la cantidad del producto
        print("Producto actualizado correctamente.")  # Mensaje de confirmación
        
        
def eliminar_producto(inventario,eliminar_p):  # Función para eliminar un producto
    for producto in inventario:  # Recorre el inventario
            if producto['Nombre'].lower() == eliminar_p.lower():  # Busca coincidencia por nombre
                print('Producto encontrado')  # Mensaje si lo encuentra
                inventario.remove(producto)  # Elimina el producto de la lista
                print(f'Producto {producto['Nombre']} eliminado')  # Muestra mensaje de eliminación
            
    print(f'Producto {eliminar_p} no existe')  # Mensaje si no se encontró el producto
    
    
def calcular_estadisticas(inventario):  # Función para calcular estadísticas del inventario
    p_totales = len(inventario)  # Cuenta la cantidad total de productos
    suma_total = sum(productos['Precio'] * productos['Cantidad'] for productos in inventario)  
    # Calcula el valor total del inventario (precio * cantidad de cada producto)

    producto_mas_caro = max(inventario, key=lambda x: x['Precio'])  
    # Encuentra el producto con mayor precio

    producto_mayor_stock = max(inventario, key=lambda x: x['Cantidad'])  
    # Encuentra el producto con mayor cantidad

    return {  # Devuelve un diccionario con los resultados
        'Productos totales': p_totales,  # Total de productos
        'Valor total': suma_total,  # Valor total del inventario
        'Producto mas caro': f'Nombre: {producto_mas_caro['Nombre']} || Precio: {producto_mas_caro['Precio']}$',
        # Muestra el producto más caro

        'Producto mayor stock': f'Nombre: {producto_mayor_stock['Nombre']} || Cantidad: {producto_mayor_stock['Cantidad']} unidades'
        # Muestra el producto con mayor cantidad
        }