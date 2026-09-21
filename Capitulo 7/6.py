entrada = input("Ingresa un número entero: ")

try:
    numero = int(entrada)
except ValueError:
    print("Error: No ingresaste un entero válido.")
else:
    print("Conversión exitosa")
finally:
    print("Fin del programa")
