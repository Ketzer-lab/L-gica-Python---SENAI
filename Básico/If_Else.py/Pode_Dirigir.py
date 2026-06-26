# Verificar se uma pessoa pode dirigir

idade = int(input("Qual a sua idade? "))
habilitacao = True

pode_dirigir = idade >= 18 and habilitacao
print(f"Pode dirigir: {pode_dirigir}")