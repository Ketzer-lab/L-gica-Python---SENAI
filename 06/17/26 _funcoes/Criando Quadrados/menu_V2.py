altura = 1
largura = 16

palavras = ("Usuários", "Clientes", "Fornecedores", "Relatórios")

def quadrados():                                    # Função que cria 1 quadrado com uma palavra no centro.
    
    print(f"+{largura*'-'}+")                       # Cria uma linha "+--------------------+"

    for linha in range(altura):                     # Cria as colunas com "|" e escreve a palavra no centro das colunas.
        if linha == altura // 2:                    # Se a linha(|) for igual a metade da altura, vai escrever uma palavra no centro do quadrado.
            print(f"|{palavra.center(largura)}|")

        else:                                       # Se não vai imprimir somente as colunas e nada no meio.
            print(f"|{largura*" "}|")

    print(f"+{largura*'-'}+")

for palavra in palavras:
    quadrados()
