
# def menu():

#     print("=== MENU PRINCIPAL ===")
#     print("1. Agregar un producto")
#     print("2. Mostrar inventario")
#     print("3. Actualizar producto")
#     print("4. Eliminar producto")
#     print("5. Calcular estadísticas")
#     print("6. Salir")




# def agregar_producto(inventario,nombre, precio, cantidad):
        
#         producto = {
#             'Nombre': nombre,
#             'Precio': precio,
#             'Cantidad': cantidad
#         }
#         inventario.append(producto)

#         print(f"Producto '{nombre}' agregado al inventario.\n")

# def ver_inventario(inventario):
#     if len(inventario) == 0:
#         print('El inventario está vacío')
#     else:
#         for i in inventario:
#             print(f'Nombre: {i['Nombre']} | Precio: {i['Precio']}$ | Cantidad: {i['Cantidad']} unidades')

# def actualizar_producto(p, N_nombre, N_precio, N_cantidad):
#         p['Nombre'] = N_nombre
#         p['Precio'] = N_precio
#         p['Cantidad'] = N_cantidad
#         print("Producto actualizado correctamente.\n")
        
        
# def eliminar_producto(inventario,eliminar_p):
#     inventario.remove(eliminar_p)
    
# def calcular_estadisticas(inventario):
#     contar = len(inventario)
#     total = sum(productos['Precio'] * productos['Cantidad'] for productos in inventario)
#     print(f'La cantidad total de productos es: {contar}')
#     print(f'El valor total del inventario es: {total}$')
#     print('')
    

