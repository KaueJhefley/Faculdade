nome = input('digite seu nome de usuario: ')
senha = input('digite sua senha')
while nome == senha:
    print('senha deve ser diferente do nome de usuario')
    nome = input('digite seu nome de usuario: ')
    senha = input('digite sua senha')