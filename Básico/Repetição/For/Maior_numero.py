#Código para decidir o maior de 5 números.

maior = None
for i in range (5):
  numero = int(input(f"Digite o {i+1}° número: "))

  if maior is None or numero > maior:
    maior = numero

print(f'O maior numero é {maior}.')