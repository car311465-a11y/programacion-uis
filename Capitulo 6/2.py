original = [10, 20, 30]

copia_asignacion = original
copia_metodo = original.copy()
copia_slicing = original[:]

copia_asignacion[0] = 99
copia_metodo[1] = 88
copia_slicing[2] = 77

print("Original:", original)
print("Copia asignación directa:", copia_asignacion)
print("Copia con .copy():", copia_metodo)
print("Copia con slicing:", copia_slicing)

