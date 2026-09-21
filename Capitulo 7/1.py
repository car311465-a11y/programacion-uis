numeros = [1, 2, 3]

try:
    print(numeros[5])
except IndexError:
    print("Error: El índice solicitado está fuera del rango de la lista.")
