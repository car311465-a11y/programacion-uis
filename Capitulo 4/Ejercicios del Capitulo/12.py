saldo = 500
while saldo > 0:
    monto_str = input(f"Saldo actual: ${saldo}. Ingresa el monto a retirar (o 0 para salir): ")
    monto = float(monto_str)
    
    if monto == 0:
        break
    elif monto > saldo:
        print("Saldo insuficiente.")
        break
    else:
        saldo -= monto
        print(f"Retiro exitoso. Saldo restante: ${saldo}")

print(f"Operación finalizada. Tu saldo final es: ${saldo}")
