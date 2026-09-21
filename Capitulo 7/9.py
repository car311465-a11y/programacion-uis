def ingresar_nota():
    while True:
        entrada = input("Ingresa una nota (0.0 a 5.0): ")
        try:
            nota = float(entrada)
            if 0.0 <= nota <= 5.0:
                return nota
            else:
                print("Error: La nota debe estar en el rango de 0.0 a 5.0.")
        except ValueError:
            print("Error: Debes ingresar un valor numérico válido.")

# Ejemplo de uso:
nota_final = ingresar_nota()
print(f"Nota registrada correctamente: {nota_final}")
