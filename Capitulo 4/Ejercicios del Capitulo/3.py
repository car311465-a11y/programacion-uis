num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operador = input("Ingresa un operador (+, -, *, /): ")

if operador == "+":
    print(f"Resultado: {num1 + num2}")
elif operador == "-":
    print(f"Resultado: {num1 - num2}")
elif operador == "*":
    print(f"Resultado: {num1 * num2}")
elif operador == "/":
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Error: Operador no válido.")
