# Sistema de Inventario en Python

Este proyecto es un sistema de inventario en consola desarrollado en Python.  
Permite gestionar productos mediante un menú interactivo, incluyendo operaciones como agregar, buscar, actualizar, eliminar y guardar/cargar datos desde archivos CSV.

---

## Funcionalidades

El sistema permite:

1. Agregar producto
2. Mostrar inventario 
3. Buscar producto 
4. Actualizar producto
5. Eliminar producto  
6. Calcular estadísticas 
7. Guardar CSV  
8. Cargar CSV  
9. Salir  

---

## Estructura del Proyecto

El programa está dividido en varios archivos para organizar mejor el código:

proyecto/

│

├── main.py # Archivo principal (controla el programa)

├── servicios.py # Funciones del inventario (CRUD y estadísticas)

├── archivos.py # Manejo de archivos CSV

---

##  ¿Cómo funciona?

### 1. Archivo principal (`main.py`)

Este archivo controla todo el flujo del programa:

- Muestra el menú
- Recibe la opción del usuario
- Llama a las funciones correspondientes

#### Flujo general:

1. Se crea una lista vacía llamada `inventario`
2. Se ejecuta un bucle infinito (`while True`)
3. Se muestra el menú
4. El usuario elige una opción
5. Dependiendo de la opción:
   - Se ejecuta una función de `servicios.py`
   - O se usa `archivos.py` para guardar/cargar datos

---

### 2. Archivo `servicios.py`

Aquí están las funciones principales del inventario.

#### Funciones:

- `menu()`: Muestra el menú en pantalla  
- `agregar_producto()`: Agrega un producto al inventario  
- `ver_inventario()`: Muestra todos los productos  
- `buscar_producto()`: Busca un producto por nombre  
- `actualizar_producto()`: Modifica los datos de un producto  
- `eliminar_producto()`: Elimina un producto  
- `calcular_estadisticas()`: Calcula datos como:
  - Total de productos
  - Valor total del inventario
  - Producto más caro
  - Producto con mayor stock  

#### Estructura de un producto:

Cada producto es un diccionario:

```python
{
    "Nombre": "Arroz",
    "Precio": 2500,
    "Cantidad": 10
}
```
Y todos los productos se almacenan en una lista:
```
inventario = [producto1, producto2, ...]
```

### 3. Archivo `archivos.py`

Este archivo se encarga de trabajar con archivos CSV.

Funciones:
guardar_csv(inventario, ruta)
Guarda el inventario en un archivo CSV
cargar_csv(ruta, inventario_actual)
Carga datos desde un CSV y permite:
Reemplazar el inventario actual
O combinar los datos

### Librerías utilizadas
`time`
Se usa para pausar el programa (`sleep`)
Ejemplo:
```
time.sleep(1)
```
`csv`
Permite leer y escribir archivos CSV
Se usa en archivos.py

### Validaciones implementadas

El programa incluye validaciones para evitar errores:

* Verifica que el usuario ingrese números válidos
* Evita nombres vacíos
* Controla errores al leer archivos
* Maneja excepciones (`try/except`)

### Ejemplo de uso
```
=== MENU PRINCIPAL ===
1. Agregar un producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Calcular estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
Ingrese una opción
1
Nombre del producto: ejemplo
Ingrese el precio: 1500
Ingrese la cantidad: 2
Producto 'ejemplo' agregado al inventario.
```
### Requisitos
* Ejecutar en consola o terminal
* Este proyecto usa un entorno virtual para aislar las dependencias.

### Crear entorno virtual:
```bash
python -m venv venv
```
Activar entorno virtual:
En Windows:
```
venv\Scripts\activate
```
En Linux/Mac:
```
source venv/bin/activate
```

### Archivo `requirements.txt`

Este archivo contiene las librerías necesarias del proyecto.

Para instalar todo:
```
pip install -r requirements.txt
```
