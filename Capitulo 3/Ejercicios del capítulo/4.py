mi_tupla = (1, 2, 3)
try:
    mi_tupla[0] = 10
except TypeError as e:
    print(e)
