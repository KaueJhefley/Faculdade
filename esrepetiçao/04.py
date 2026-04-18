po_a = 80000
po_b = 200000
ano = 0
while po_a <= po_b:
    ano = ano + 1
    crecimento_a = po_a * (3/100)
    crecimento_b = po_b * (1.5/100)
    po_a = po_a + crecimento_a
    po_b = po_b + crecimento_b
print (f'demorou {ano} anos para a populaçao do pais A superar a do pais B')