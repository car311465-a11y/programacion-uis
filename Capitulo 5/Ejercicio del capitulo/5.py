contador = 0

def incrementar_contador():
    global contador
    contador += 1
    print(f"Fue necesario usar 'global' porque se modificó la variable fuera del scope local. Contador: {contador}")

incrementar_contador()
