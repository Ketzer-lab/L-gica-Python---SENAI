cinema = []

linhas = 5
colunas = 10

soma = 0

for i in range(linhas):
  linha = []
  for j in range(colunas):
    linha.append("L")
  cinema.append(linha)


linha_escolhida = int(input("Digite que linha você deseja (1-5): "))
coluna_escolhida = int(input("Digite que coluna você deseja (1-10): "))

cinema[linha_escolhida-1][coluna_escolhida-1] = "O"

for linha in cinema:
    for elemento in linha:
        print(f'[{elemento}]', end="\t")
        if elemento == "O":
            soma += 1
    print()