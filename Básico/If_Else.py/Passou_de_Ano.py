# Verificar se o sujeito passou de ano na escola 'X'

nota_final = float(input("Qual foi a sua nota final? "))
faltas = int(input("Quantas faltas você teve? "))

passou_de_ano = nota_final >= 7 and faltas <= 50
print("Parabéns, você passou de ano.")