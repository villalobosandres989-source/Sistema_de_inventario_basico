# Sistema_de_inventario_basico
Simulador de sistema de inventario por consola para el manejo de productos.

# 🚀 Funcionalidades
* Solicita al usuario:
  * 🏷️ Nombre del producto
  * 💲 Precio del producto
  * 🔢 Cantidad de unidades
* Calcula el precio total
* Muestra en pantalla el producto agregado con su resumen
# 🧠 Lógica del programa
El sistema:
1. Pide los datos al usuario mediante `input()`
2. Convierte los valores numéricos a tipos adecuados (`float` y `int`)
3. Calcula el total:
   ```
   total = precio * cantidad
   ```
4. Imprime un resumen del producto agregado

# 🖥️ Ejemplo de uso
```
Ingrese el nombre del producto: Pera
Ingrese el precio del producto: 1.200
ingrese la cantidad: 3

producto agregado correctamente
Producto: Pera
Precio: 1.200
Cantidad: 3
Precio total: $3.600
```
# 🧩 Código del programa

```
nombre = ""
precio = 0.0
cantidad = 0

nombre = input("Ingrese el nombre: ")


while True:
    try:
        precio = float(input("Ingresa el precio: "))
        break
    except ValueError:
        print("Valor inválido, ingrese un número válido")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        break
    except ValueError:
        print("Valor inválido, ingrese un número entero")


costo_total = precio * cantidad

print("\nDatos ingresados:")
print(f"Producto: {nombre} || Precio: {precio:.3f} $|| Cantidad: {cantidad} || Costo total: {costo_total:.3f} $")
```
# 🛠️ Requisitos
* Python 3.x
* Ejecutar en consola o terminal
