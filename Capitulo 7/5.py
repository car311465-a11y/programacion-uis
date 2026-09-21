def pedir_edad():
    try:
        edad = int(input("Ingresa tu edad: "))
        if 0 <= edad <= 120:
            return edad
        else:
            print("Advertencia: La edad debe estar en el rango de 0 a 120 años.")
    except ValueError:
        print("Advertencia: Por favor ingresa un número entero válido.")

# Ejemplo de uso:
pedir_edad()
