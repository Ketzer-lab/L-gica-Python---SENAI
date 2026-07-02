def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    # Linhas
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True

    # Colunas
    for col in range(3):
        if all(tabuleiro[lin][col] == jogador for lin in range(3)):
            return True

    # Diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True

    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        mostrar_tabuleiro(tabuleiro)

        try:
            linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0-2): "))
            coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0-2): "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if linha not in range(3) or coluna not in range(3):
            print("Posição inválida!")
            continue

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada!")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"🎉 Jogador {jogador_atual} venceu!")
            break

        if jogadas == 9:
            mostrar_tabuleiro(tabuleiro)
            print("🤝 Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

jogo_da_velha()