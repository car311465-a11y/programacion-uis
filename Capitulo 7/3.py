entrada = input("Ingresa un número entero: ")

try:
    numero = int(entrada)
    print(f"Número ingresado: {numero}")
except ValueError:
    print("Error: El valor ingresado no se puede convertir a entero.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
