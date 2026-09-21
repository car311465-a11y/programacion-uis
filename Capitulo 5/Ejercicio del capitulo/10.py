def leer_numeros():
    entrada = input("Ingresa números separados por comas: ")
    return [int(x.strip()) for x in entrada.split(",")]

def calcular_estadisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return minimo, maximo, promedio

def mostrar_resultado(minimo, maximo, promedio):
    print(f"Mínimo: {minimo}")
    print(f"Máximo: {maximo}")
    print(f"Promedio: {promedio:.2f}")

numeros = leer_numeros()
min_val, max_val, prom_val = calcular_estadisticas(numeros)
mostrar_resultado(min_val, max_val, prom_val)
