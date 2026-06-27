estoque = {
    "Alface": [10, 0.45],
    "Batata": [5, 1.20],
    "tomate": [8, 2.30],
    "Feijão": [3, 1.50]
}

# Ler quantidade e preço
qtd = estoque["Alface"][0]    #10
preco = estoque["Alface"][1]  #0.45

# Atualizar após uma venda
estoque["Alface"][0] -= 2     #Agora restam 8 unidades

# Atualizar preço
estoque["Batata"][1] = 1.35