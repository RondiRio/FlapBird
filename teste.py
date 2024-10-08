notaB1 = input("Entre com a nota do 1º bimestre")
notaB2 = input("Entre com a nota do 2º bimestre")
notaB3 = input("Entre com a nota do 3º bimestre")
notaB4 = input("Entre com a nota do 4º bimestre")
qtd_bimestre = 4
min = 6
min_rec = 5.0
calculo_media = (int(notaB1) + int(notaB2) + int(notaB3) + int(notaB4)) / qtd_bimestre
# se calculo_media for menor ou igual  a min, mostra reprovado, se for menor que 6 e maior que 5 mostra em recuperacao se nao, mostra reprovado

if calculo_media < 6 and calculo_media > min_rec:
    print("Recuperação")
elif calculo_media < min_rec:
    print("Reprovado")
else:
    print("Aprovado com a nota \n ", calculo_media)
