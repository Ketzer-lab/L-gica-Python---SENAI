impar = (1, 3, 5, 7, 9)
par = (0, 2, 4, 6, 8,)
contadorI = 0
contadorP = 0


for i in range (10):
  numero= int(input(f"Digite o {i+1}° número: "))

for i in numero:
  if i in impar:
    contadorI += 1
  else:
    contadorP  += 1
print(f"Você digitou {contadorI} números impares e {contadorP} números pares.")