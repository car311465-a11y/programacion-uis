
def imprimir_clave_valor(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_clave_valor(nombre="Luis", edad=20, ciudad="Barbosa")

