maior = 0
for i in range(5):
    num = int(input('informe um numero: '))
    if maior == 0 and num > maior:
        maior = num
print(maior)