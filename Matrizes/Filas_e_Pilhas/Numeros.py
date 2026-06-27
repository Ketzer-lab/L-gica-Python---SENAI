pilha = []

for i in range(5):
  numero = int(input("Escreva um número: "))
  pilha.append(numero)

for i in range(2):
  pilha.pop()

print(pilha)