fila = []

for i in range(3):
  nomes = input("Escreva um nome: ")
  fila.append(nomes)                    # Precisa estar dentro do mesmo for, porque caso contrario o código ira separar as letras dos nomes
print(f'Fila atual: {fila}')

nome_removido = fila.pop(0)             # Remove o primeiro nome e da um 'nome' ao nome removido.

print(f'Fila final: {fila}')
print(f'Nome removido: {nome_removido}')