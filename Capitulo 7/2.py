entrada = input("Ingresa un número entero: ")

try:
    numero = int(entrada)
    print(f"Número ingresado: {numero}")
except ValueError:
    print("Entrada inválida: debe ser un número entero")
