po_a = int(input('informe a populaçao do pais A: '))
po_b = int(input('informe a populaçao do pais B: '))
taxa_a = float(input('informe a taxa de crescimento do pais A: '))
taxa_b = float(input('informe a taxa de crescimento do pais B: '))
ano = 0
while po_a <= po_b:
    ano = ano + 1
    crecimento_a = po_a * (taxa_a/100)
    crecimento_b = po_b * (taxa_b/100)
    po_a = po_a + crecimento_a
    po_b = po_b + crecimento_b
print (f'demorou {ano} anos para a populaçao do pais A superar a do pais B')