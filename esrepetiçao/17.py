num = int(input('informe um numero: '))
fatorial = 1 
for i in range(num, 1, -1):
    fatorial = i * fatorial
print(f"O fatorial de {num} é {fatorial}")
