texto = input("Digite um texto:")
vogais = ("AEIOUaeiou")
contador = 0

for letra in texto:
  if letra in vogais:
    contador += 1

print(f'O seu texto tem {contador} vogais.')