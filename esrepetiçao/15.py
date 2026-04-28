termos = int(input("Digite o numero de termos da série de Fibonacci: "))
numero = 1
numero_anterior = 0
for i in range(termos):
    print(numero)
    aux = numero
    numero += numero_anterior
    numero_anterior = aux