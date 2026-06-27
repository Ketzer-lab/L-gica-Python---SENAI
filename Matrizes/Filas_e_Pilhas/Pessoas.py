fila = []

numero_de_pessoas = int(input("Quantas pessoas tem na fila? "))

for i in range(numero_de_pessoas):
  nomes = input("Qual o nome das pessoas na fila ")
  fila.append(nomes)

atendendo = fila.pop(0)
print(f'Atendendo: {atendendo}')

if not fila:
  print("Fila vazia ")

print(fila)