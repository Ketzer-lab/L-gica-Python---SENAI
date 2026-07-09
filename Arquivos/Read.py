# Le e printa o que esta esceito dentro de um arquivo

with open("exemplo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

print()

with open ("exemplo.txt", "r") as f:
    linha1 = f.readline()
    linha2 = f.readline()
    print(linha1)

print()

with open("exemplo.txt", "r") as f:
    linhas = f.readlines()
    for linha in linhas:
        print(linha.strip())

print()

with open("exemplo.txt", "r") as f:
    for linha in f:
        print(linha)