texto = "Aprender a programar en Python es excelente"
contador = 0
for caracter in texto:
    if caracter == "a":
        contador += 1
print(f"La letra 'a' aparece {contador} veces.")
