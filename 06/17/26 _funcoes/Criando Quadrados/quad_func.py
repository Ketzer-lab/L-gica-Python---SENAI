altura = int(input("Altura do quadrilátero: "))
largura = int(input("Largura do quadrilátero: "))

def linha():
    """Docstring: Imprime uma linha +----+"""
    print(f'+{largura*'-'}+')
    return

def coluna():
    """Docstring: Imprime uma coluna |    |"""
    for _ in range(altura):
        print(f'|{largura*" "}|')
    return

print(linha(), coluna(), linha())