numero = int(input("Digite um número."))
contador = 1 # Uma variavel sempre deve começar com algum valor caso contrario não sera possível aumentar um valor inexistente.

while contador <= 10:
  print(f'{numero} x {contador:2} = {numero*contador}')  # O ':2' é desnecessario, ele esta ali apenas para alinhar as casasa decimais.
  contador += 1