fila = []

while True:
  print("\n1 -Adicionar Pessoa ")
  print("2 -Atender Pessoa ")
  print("3 -Sair ")

  opcao = input("Escolha ")

  if opcao == "1":
    nome = input("Nome: ")
    fila.append(nome)

  elif opcao == "2":
    if not fila:
      print("Fila Vazia ")
    else:
      print(f'Atendendo: {fila.pop(0)}')

  elif opcao == "3":
    break

  else:
    print("Opção inválida ")