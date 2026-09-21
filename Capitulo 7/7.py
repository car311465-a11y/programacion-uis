def calcular_promedio(lista):
    try:
        assert len(lista) > 0, "La lista no puede estar vacía"
        return sum(lista) / len(lista)
    except AssertionError as error:
        print(error)

# Ejemplos de uso:
calcular_promedio([])
print(calcular_promedio([10, 20, 30]))
