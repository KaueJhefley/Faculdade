numero = 1
numero_anterior = 0
for i in range(1, 501):
    print(numero)
    aux = numero
    numero += numero_anterior
    numero_anterior = aux