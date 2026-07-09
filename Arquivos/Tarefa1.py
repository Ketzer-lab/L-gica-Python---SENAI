nomes =[]

for i in range(3):
    nome = input("Escreva um nome: ")
    nomes.append(nome)
with open("Fila_de_nomes.txt", "w") as f:
    for name in nomes:
        f.write(name + "\n")