
altura = 1
largura = 16

palavras = ("Usuários", "Clientes", "Fornecedores", "Relatórios")

def linhas():
    """Cria uma linha +-----+"""
    print(f"+{largura*'-'}+")

def colunas():
    """Cria duas colunas com uma palavra no centro | palavra |"""
    for linha in range(altura):
        if linha == altura // 2:
            print(f"|{palavra.center(largura)}|")
        else:
            print(f"|{largura*" "}|")
for palavra in palavras:
    linhas()
    colunas()
linhas()