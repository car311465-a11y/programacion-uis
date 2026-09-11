suma_total = 0
while True:
    entrada = input("Ingresa un número (o escribe 'salir' para terminar): ")
    if entrada.lower() == "salir":
        break
    suma_total += float(entrada)
print(f"La suma total es: {suma_total}")
