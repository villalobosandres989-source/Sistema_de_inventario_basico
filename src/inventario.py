
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