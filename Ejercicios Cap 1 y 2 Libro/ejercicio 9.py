nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")
print(f"Hola {nombre}, tienes {edad} años.")

# Ejercicio 10
try:
    numero = int("Hola")
except ValueError as e:
    print(e)
