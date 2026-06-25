
altura = 3
largura = 20
palavra = "Usuario"

def quadrado(altura, largura):
    print(f"+{largura*'-'}+")

    for linha in range(altura):
        if linha == altura // 2:
            print(f"|{palavra.center(largura)}|")
        else:
            print(f"|{largura*" "}|")

    print(f"+{largura*'-'}+")