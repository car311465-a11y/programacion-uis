aprobado = input("¿Aprobó el curso introductorio? (si/no): ").strip().lower() == "si"
promedio = float(input("Ingrese su promedio: "))
print(aprobado and promedio >= 3.5)
