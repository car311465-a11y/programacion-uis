def es_par():
    numero = int(input("Digite su número: "))
    if numero%2 == 0:
        par = True
    else:
        par = False
    return par

igual = es_par ()

if igual == True:
    print("El número es par")
elif igual == False:
    print("El número no es par")



    
    
