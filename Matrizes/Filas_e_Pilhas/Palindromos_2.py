palavra = input("Digite uma palavra: ")
pilha = []

#empilha caracteres
for letra in palavra:
  pilha.append(letra)

#monta palavra invertida
invertida = ""
while pilha:
  invertida += pilha.pop()

#verificação
if palavra == invertida:
  print("É palíndromo! ")
else:
  print("Não é um palíndromo")