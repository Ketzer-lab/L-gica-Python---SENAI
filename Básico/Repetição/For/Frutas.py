#Pergunta sobre frutas usando o laço 'for'

frutas = ("(A) Maçã", "(B) Pera", "(C) Banana")

for f in frutas:
  print(f)
fav = input("Qual dessas frutas você mais gosta?\n")
if fav == 'A'.lower():
  print("Que original. ")
elif fav == 'B'.lower():
  print("Esquisito.")
elif fav == 'C'.lower():
  print("Banana é?")
else:
  print("Opção invalida, tente novamente")