largura = 20

def desenha_linha(limite, preenchimento, largura):
    print(limite + (preenchimento * (largura - 2)) + limite)

def montar_menu(itens, largura):
    desenha_linha('+', '-', largura)
    for item in itens:
        #gera o item alinhado á esquerda (<) e largura 16
        print(f'| {item:<16} |')
        #se ão é o último item, desenha a linha de separação
        if item != itens[-1]:
            desenha_linha('+', '-', largura)
    desenha_linha('+', '-', largura)

itens = ['Usuário', 'Clientes', 'Fornecedores', 'Relatórios']
item_largura = 20
montar_menu(itens, item_largura)