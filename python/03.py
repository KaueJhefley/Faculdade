nome = input('digite seu nome: ')
while len(nome) < 3:
    print('nome invalido')
    nome = input('digite seu nome: ')

idade=int(input("informe a idade--> "))
while ( idade > 150 or idade < 0 ):
    print('idade invalida')
    idade=int(input("informe a idade--> "))


salario=float(input("informe um salário--> "))
while ( salario < 0 ):
     print('invalido')
     salario=float(input("informe um salário--> "))
    

sexo=str(input("informe a inicial do seu sexo--> "))
while  sexo !="f" and sexo!="m" :
    print('invalido')
    sexo=str(input("informe a inicial do seu sexo--> "))


e_civil = input('informe seu estado civil: ')
while e_civil != 's' and e_civil != 'c' and e_civil != 'v' and e_civil != 'd':
    print ('invalido')
    e_civil = input('informe seu estado civil: ')

