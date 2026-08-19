par = 0 
impar= 0
for i in range(10):
    num = int(input('informe um numero: '))
    if num % 2 != 0:
        impar = impar + 1
    else: 
        par = par + 1
print(par, impar)