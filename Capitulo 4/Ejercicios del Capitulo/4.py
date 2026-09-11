contrasena_correcta = "python123"
contrasena = input("Ingresa la contraseña: ")
while contrasena != contrasena_correcta:
    contrasena = input("Contraseña incorrecta. Intenta de nuevo: ")
print("Contraseña correcta. ¡Acceso concedido!")
