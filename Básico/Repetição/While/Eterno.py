n = int(input("Digite um número: ")) # Dessa froma ira perguntar eternamente um número.
x = 1
while x != "...":
  print(x)
  input("Digite um número: ")
  x = x + 1             # Ao invés de usar x = x + 1 pode se usar x += 1, que será a exata mesma coisa só que abreviado. Também pode ser usado com -=, *=, /=.