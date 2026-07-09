# Cria um arquivo e escreve o que for ordenado dentro.

with open("saida1.txt", "w") as f:
    f.write("Ola, mundo!\n")
    f.write("Segunda linha.\n")

linhas = ["Linha 1\n",
          "Linha 2\n",
          "Linha 3\n"]
with open("saida2.txt", "w") as f:
    f.writelines(linhas)

nomes = ["Ana", "Bruno", "Carlos"]
with open("saida3.txt", "w") as f:
    for nome in nomes:
        f.write(nome + "\n")
    