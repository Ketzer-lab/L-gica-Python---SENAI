fila = []
historico = []
dicionario = {}

while True:
  print("\n1 -Adicionar cliente: ")             # \n serve para deixar uma linha em branco antes do texto.
  print("2 -Atender cliente: ")
  print("3 -Mostrar fila: ")
  print("4 -Mostrar histórico: ")
  print("5 -Buscar cliente: ")
  print("6 -Sair")

  opcao = input("Escolha: ")

  if opcao == "1":
    nome = (input("Nome do cliente: "))
    if not nome.replace(" ", "").isalpha():       # O comando '.replace(" ", "")' troca o " "(espaço) por ""(nada), pois o .isalpha aceita apenas letras. O .isalpha força o código a ceitar somente letras não números ou outros caracteres.
      print("Nome inválido, tente novamente.")
    else:
      idade = int(input("Idade do cliente: "))
      if idade < 0:                               # Impede que o usuário coloque uma pessoa com uma idade impossível na fila.
        print("Idade ireal, tente novamente ")
      else:
        dicionario[nome] = idade
        fila.append(nome)

  elif opcao == "2":
    if len(fila) > 0:                           # Imprime "Não há clientes na fila." ao invés de imprimir "{}".
      cliente = fila.pop(0)
      print(cliente)
      historico.append(cliente)
    else:
      print("Não há clientes na fila.")

  elif opcao == "3":
    if len(fila) > 0:
      print(dicionario)
    else:
      print("Não há clientes na fila.")

  elif opcao == "4":
    if len(historico) > 0:
      print(historico)
    else:
      print("Histórico vazio.")

  elif opcao == "5":
    nome_ver = input("Digite um nome: ")
    if nome_ver in fila:
      print("Cliente em espera.")
    elif nome_ver in historico:
      print("Cliente atendido.")
    else:
      print("Cliente não existente.")     # Confere se o nome exigido existe no sistema.

  elif opcao == "6":
    break

  else:
    print("Opção inválida!")