altura = 3
largura = 20
U = "Usuários"
C = "Clientes"
F = "Fornecedores"
R = "Relatórios"
palavras = ("Usuários")

def linhas():
    print(f"+{largura*'-'}+")

def colunas():
    for linha in range(altura):
        if linha == altura // 2:
            print(f"|{palavra.center(largura)}|")
        else:
            print(f"|{largura*" "}|")

print(linhas(), colunas(), linhas())