# Tirado da internet para estudos: Como fazer um gráfico

import matplotlib.pyplot as plt

# 1. Pedir os dados ao usuário
# O usuário deve digitar os números separados por espaço: 1 2 3 4
x_input = input("Digite os valores do Eixo X separados por espaço: ")
y_input = input("Digite os valores do Eixo Y separados por espaço: ")

# 2. Converter a string de entrada em uma lista de números (floats)
x = [float(i) for i in x_input.split()]
y = [float(i) for i in y_input.split()]

# 3. Verificar se as listas têm o mesmo tamanho
if len(x) != len(y):
    print("Erro: O número de elementos em X e Y deve ser igual.")
else:
    # 4. Criar o gráfico
    plt.figure(figsize=(8, 5)) # Define o tamanho da janela
    plt.plot(x, y, marker='o', linestyle='-', color='b') # Linha com pontos

    # 5. Customizar o gráfico (Títulos e Labels)
    plt.title("Gráfico Simples com Dados do Usuário")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.grid(True) # Adiciona grade

    # 6. Exibir o gráfico
    plt.show()