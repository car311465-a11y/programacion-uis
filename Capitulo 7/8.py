def validar_producto(producto):
    claves_requeridas = ["nombre", "precio", "cantidad"]
    
    for clave in claves_requeridas:
        if clave not in producto:
            print(f"Falta la clave: '{clave}'")

# Ejemplo de uso:
prod_incompleto = {"nombre": "Laptop", "precio": 1200}
validar_producto(prod_incompleto)
