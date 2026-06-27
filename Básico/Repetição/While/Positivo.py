# Solicita um número positivo, se for negativo, pede de novo
numero = -1
while numero < 0:
    numero = int(input("Digite um número positivo: "))
print(f"Obrigado! Você digitou {numero}")