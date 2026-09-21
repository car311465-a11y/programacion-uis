productos = ['Pan', 'Leche', 'Huevos']
precios = [1500, 3200, 5200]

lista_formateada = [f"{producto}: ${precio}" for producto, precio in zip(productos, precios)]
productos_costosos = [f"{producto}: ${precio}" for producto, precio in zip(productos, precios) if precio > 3000]

print("Todos los productos:", lista_formateada)
print("Productos con precio mayor a $3000:", productos_costosos)
