def calcular_media(numeros):
    """Recebe uma lista de numeros inteiros e retorna a média aritmética."""
    if not numeros:
        return 0.0
    total = sum(numeros)
    return float(total) / len(numeros)

exemplo = [7, 8, 9, 10]
resultado = calcular_media(exemplo)
print(resultado)