tabela = {
    "Alface": 0.45,
    "Batata": 1.20,
    "tomate": 2.30,
    "Feijão": 1.50
}

print("Batata" in tabela) #True
print("Manga" in tabela) #False

tabela.get("manga", -1) # Retorna um valor padrão se a chave não existir
del tabela["Alface"] # Deleta "Aface" da tabela
tabela["Alface"] = 1 # Adicona "Alface" á tabela