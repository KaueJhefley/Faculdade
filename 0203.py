idade=int(input('digite sua idade '))

if idade >= 18:
    print('esse usuario pode digirir')
    psico= input('no psicotecnico voce acertou aquele moi de tracinho?')
    if psico == 'sim':
        print('voce pode tirar a cnh ')
    else:
        print('voce nao pode tirar a cnh ')
   

else:
    print('esse usuario nao pode digirir')