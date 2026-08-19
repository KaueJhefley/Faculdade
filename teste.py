bovinos = []
suinos = []
aves = []

while True:
    op = input('------O que deseja fazer?------ \n'
               '1-Cadastrar Animal \n'
               '2-Buscar Animal \n'
               '0-Sair \n')

    if op == '0':
        print('Programa finalizado')
        break

    if op == '1':
        tipo = input('----Que tipo de animal deseja registrar---- \n'
                     '1-bovino \n'
                     '2-suino \n'
                     '3-ave \n')

        identificacao = input('Digite a identificação do animal: ')
        status = input('Digite o Status do animal: ')
        animal = [identificacao, status]

        if tipo == '1':
            lista = bovinos
        elif tipo == '2':
            lista = suinos
        elif tipo == '3':
            lista = aves
        else:
            print('Tipo inválido')
            continue

        # verificar se já existe
        existe = False
        for a in lista:
            if a[0] == identificacao:
                existe = True
                break

        if existe:
            print('Animal já existente')
        else:
            lista.append(animal)
            print('Animal cadastrado')

    elif op == '2':
        tipo = input('----Que tipo de animal deseja encontrar---- \n'
                     '1-bovino \n'
                     '2-suino \n'
                     '3-ave \n')

        busca = input('Digite a identificação do animal: ')

        if tipo == '1':
            lista = bovinos
        elif tipo == '2':
            lista = suinos
        elif tipo == '3':
            lista = aves
        else:
            print('Tipo inválido')
            continue

        encontrado = False
        for a in lista:
            if a[0] == busca:
                print('Animal encontrado:', a)
                encontrado = True
                break

        if not encontrado:
            print('Animal não encontrado')







             if op == '1':
        tipo = input('----Que tipo de animal deseja registrar---- \n 1-bovino \n 2-suino \n 3-ave')
        if tipo == '1':
            identificacao = input('Digite a identificação do animal: ')
            status = input('Digite o Status do animal: ')
            animal = [identificacao, status]

            if identificacao in bovinos:
                print('animal ja existente')
            else:
                bovinos.append(animal)
                print('animal cadastrado')
        elif tipo == '2':
            identificacao = input('Digite a identificação do animal: ')
            status = input('Digite o Status do animal: ')
            animal = [identificacao, status]

            if identificacao in suinos:
                print('animal ja existente')
            else:
                suinos.append(animal)
                print('animal cadastrado')
        elif tipo == '3':
            identificacao = input('Digite a identificação do animal: ')
            status = input('Digite o Status do animal: ')
            animal = [identificacao, status]

            if identificacao in aves:
                print('animal ja existente')
            else:
                aves.append(animal)
                print('animal cadastrado')
