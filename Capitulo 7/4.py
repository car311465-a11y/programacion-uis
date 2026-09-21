def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None

# Ejemplo de uso:
print(dividir(10, 2))
print(dividir(10, 0))
