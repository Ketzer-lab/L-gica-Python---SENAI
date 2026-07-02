
def mostrar_tabuleiro(tabuleiro):
    print("\nTabuleiro:\n\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("_" * 9)
        print()

def vitória(tabuleiro, jogador):
    # Vitória por linha:
    for linha in tabuleiro:
       if all(casa == jogador for casa in linha):
           return True
    
    # Vitória por coluna:
    for col in range(3):
        if all(tabuleiro[lin][col] == jogador for lin in range(3)):
            return True
        
    # Vitória por diagonal:
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    
    if all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    
    return False

def jogo():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    jogadas = 0

    while True:
        mostrar_tabuleiro(tabuleiro)

        try:
            linha = int(input(f"Jogador {jogador_atual}, escolha uma linha (0-2): "))
            coluna = int(input(f"Jogador {jogador_atual}, escolha uma coluna (0-2): "))
        except ValueError:
            print("Digite apenas numeros!")
            continue

        if linha not in range(3) or coluna not in range(3):
            print("Posição inválida!")
            continue

        if tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada!")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if vitória(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print("Jogador {jogador_atual} venceu")
            break

        if jogadas == 9:
            mostrar_tabuleiro(tabuleiro)
            print("Empate")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

jogo()