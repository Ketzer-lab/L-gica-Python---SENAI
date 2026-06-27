texto = "PYTHON"
pilha=[]

# Empilha cada caractere
for char in texto:
  pilha.append(char)

resultado = ""

# Desempilha na ordem inversa
while pilha:
  resultado += pilha.pop()

print(resultado)