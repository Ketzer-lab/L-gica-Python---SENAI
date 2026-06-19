def linha():
    """Docstring: Cria uma linha +----+"""
    print("+", end="")
    for c in range(2, 20):
        print('-', end="")
    print('+')

def coluna():
    """Docstring: Cria duas colunas |"""
    for l in range(2, 5):
        print('|', end="")
        for c in range(2, 20):
            print(" ", end="")
        print('|')

print(linha(), coluna(), linha())