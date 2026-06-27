cantor_favorito = input("Me diga quem é o melhor cantor do mundo: ")
if cantor_favorito.lower() != "michael jackson":
  input("Não... Me diga quem é o melhor cantor do mundo:" )

while cantor_favorito.lower() != "michael jackson":   # .lower() é usado para considerar o texto como correto mesmo que esteja em letra mínuscula.
   cantor_favorito = input("QUAL O SEU CANTOR FAVORITO!? ")

else:
  print("Perfeito!")