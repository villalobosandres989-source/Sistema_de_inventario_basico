def menu():

    print("\n=== MENU PRINCIPAL ===")
    print("1. Agregar un producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular estadísticas")
    print("7. Salir")




def agregar_producto(inventario,nombre, precio, cantidad):
        
        producto = {
            'Nombre': nombre,
            'Precio': precio,
            'Cantidad': cantidad
        }
        inventario.append(producto)

        print(f"Producto '{nombre}' agregado al inventario.")

def ver_inventario(inventario):
    if len(inventario) == 0:
        print('El inventario está vacío')
    else:
        for i in inventario:
            print(f'Nombre: {i['Nombre']} | Precio: {i['Precio']}$ | Cantidad: {i['Cantidad']} unidades')
            
            
            
def buscar_producto(inventario, nombre):
    for producto in inventario:
                if producto['Nombre'].lower() == nombre.lower():
                    return producto
    print('Producto no encontrado')
    return None

def actualizar_producto(inventario, N_nombre, N_precio, N_cantidad):
        inventario['Nombre'] = N_nombre
        inventario['Precio'] = N_precio
        inventario['Cantidad'] = N_cantidad
        print("Producto actualizado correctamente.")
        
        
def eliminar_producto(inventario,eliminar_p):
    for producto in inventario:
               if producto['Nombre'].lower() == eliminar_p.lower():
                   print('Producto encontrado')
                   inventario.remove(producto)
                   print(f'Producto {producto['Nombre']} eliminado\n')
                   
                   break
               else:
                   print(f'Producto {eliminar_p} no existe')
    
    
def calcular_estadisticas(inventario):
    contar = len(inventario)
    total = sum(productos['Precio'] * productos['Cantidad'] for productos in inventario)
    producto_mas_caro = max(inventario, key=lambda x: x['Precio'])
    producto_mayor_stock = max(inventario, key=lambda x: x['Cantidad'])
    return {
        'Productos totales': contar,
        'Valor total': total,
        'Producto mas caro': f'Nombre: {producto_mas_caro['Nombre']} || Precio: {producto_mas_caro['Precio']}$',
        'Producto mayor stock': f'Nombre: {producto_mayor_stock['Nombre']} || Cantidad: {producto_mayor_stock['Cantidad']} unidades'
        }
    