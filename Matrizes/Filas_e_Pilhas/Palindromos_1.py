fila = []
palavra = input("Escreva uma palavra: ")

for char in palavra:
  fila.append(char)

palindromo = True

while len(fila) > 1:
  primeiro = fila.pop(0)
  ultimo = fila.pop()

  if primeiro != ultimo:
    palindromo = False
    break

if palindromo:
  print(f'{palavra} é um palíndromo! ')
else:
  print(f'{palavra} não é um palíndromo! ')