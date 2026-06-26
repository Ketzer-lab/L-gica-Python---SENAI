nota1 = input("informe a primeira nota: ")
nota2 = input("informe a segunda nota: ")
nota3 = input("informe a terceira nota: ")

# Substitui vírgulas por pontos antes de converter para float
media = ((float(nota1.replace(',', '.')) + float(nota2.replace(',', '.')) + float(nota3.replace(',', '.'))) / 3)

print("A sua média é", media)