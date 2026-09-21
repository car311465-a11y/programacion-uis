cuadrados = [x**2 for x in range(1, 11)]
pares = [x for x in range(1, 21) if x % 2 == 0]
multiplos_tres = [x for x in [3 * i for i in range(1, 15)] if x > 10][:10]

print("Cuadrados:", cuadrados)
print("Pares:", pares)
print("Múltiplos de 3 mayores a 10:", multiplos_tres)

