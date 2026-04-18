altura= float(input('digite sua altura '))
peso= float(input('digite seu peso '))
imc= peso/altura**2
if imc >= 25:
    if imc < 30:
        print('obeso')
    else:
        print('sobrepeso')
else:
    print('normal')