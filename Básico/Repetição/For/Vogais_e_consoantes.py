#Código para analizar quantas vogais e consoantes existem em um texto

texto = input("Digite um texto:")
texto = texto.lower()
vogais = ("aeiouàáãâéèêíìîóòõôúùû")
consoantes = ("qwrtýpsdfghjklçzxcvbnm")
contadorV = 0
contadorC = 0

if texto == "abacate":
  print("faz coco bonito")

for letra in texto:
  if letra in vogais:
    contadorV += 1
  if letra in consoantes:
    contadorC += 1


print(f'O seu texto tem {contadorV} vogais e {contadorC} consoantes.')