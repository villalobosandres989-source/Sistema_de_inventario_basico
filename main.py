
# Inicializar las variables nombre, precio y cantidad
nombre = ""
precio = 0.0
cantidad = 0

# Solicitar el nombre del producto al usuario

nombre = input("Ingrese el nombre del producto: ")

# Bucle para solicitar el precio hasta que el usuario ingrese un número válido

while True:
    try:
        precio = float(input("Ingresa el precio: "))
        break
    except ValueError:
        print("Valor inválido, ingrese un número válido")
        
# Bucle para solicitar la cantidad hasta que el usuario ingrese un número entero válido

while True:
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        break
    except ValueError:
        print("Valor inválido, ingrese un número entero")
        
# Calcular el costo total multiplicando el precio por la cantidad

costo_total = precio * cantidad

# Mostrar la información del producto y el costo total formateado

print("\nDatos ingresados:")
print(f"Producto: {nombre} || Precio: {precio:.3f} $|| Cantidad: {cantidad} || Costo total: {costo_total:.3f} $")

