estoque = {
    "Picanha 1Kg": 68.83,
    "Bacon 1Kg": 34.47,
    "Feijão 1Kg": 42.68,
    "Melancia 1Kg": 38.79
}

produto = input("Que produto você deseja: ")


if produto in estoque:
  preco = estoque[produto]    # Preco precisa estar dentro do if, porque caso contrario ele buscara o preço de um produto que não está no estoque e por isso não existe, dando erro
  print(f'O produto {produto} etsá em estoque e está custando {preco} reais.')
else:
  print("O prduto não é vendido na loja ou não está em estoque.")