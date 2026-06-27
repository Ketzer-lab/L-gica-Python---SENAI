#Código para analizar quantas vogais existem em um texto

texto = input("Digite um texto:")
texto = texto.lower()
vogais = ("aeiouàáãâéèêíìîóòõôúùû")
contador = 0

for letra in texto:
  if letra in vogais:
    contador += 1

print(f'O seu texto tem {contador} vogais.')