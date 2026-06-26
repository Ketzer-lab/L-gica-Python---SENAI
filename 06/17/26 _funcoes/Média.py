def calcular_media():
    """Calcula a média de uma lista de números."""
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / len(numeros)
    return media

numeros = [7, 8, 9, 10]
print(calcular_media())