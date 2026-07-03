
def mostrar_tabuleiro(tabuleiro):           # Como o nome da função já explica, o objetivo dela é criar o tabuleiro do jogo da velha.
    print("\nTabuleiro:\n\n")               # Imprime no painel a palavra "Tabuleiro:", o "\n" é utilizado para pular uma linha.
    for i in range(3):                      # Define uma repetição númerica para "i" de 0 a 2.
        print(" | ".join(tabuleiro[i]))     # Imprime "|" para formar as colunas do tabulerio, o ".join()" pega os elementos e coloca "|" entre eles.
        if i < 2:                           # Como existem 3 linhas no tabuleiro, esse comando imprime as linhas de separação depois da 1° e 2° linha.
            print("_" * 9)
        print()

def vitória(tabuleiro, jogador):                                        # Função responsável por estabelecer a vitória.
    # Vitória por linha:
    for linha in tabuleiro:                                             # Se todas as casas de uma linha forem ocupadas por um mesmo jogador (X ou O) ele ganha.
       if all(casa == jogador for casa in linha):
           return True
    
    # Vitória por coluna:
    for col in range(3):                                                # Se todas as casas em uma coluna forem ocupadas por um mesmo jogador ele ganha.
        if all(tabuleiro[lin][col] == jogador for lin in range(3)):     # "tabuleiro[lin][col]" le a linha e coluna que se encontram.
            return True
        
    # Vitória por diagonal:
    if all(tabuleiro[i][i] == jogador for i in range(3)):               # le o ponto onde linha e coluna de mesmo numero se encontram, formando uma diagonal.
        return True
    
    if all(tabuleiro[i][2-i] == jogador for i in range(3)):             # Fas os mesmo que o acima, mas subtrai 2 do valor referente a coluna, invertendo a diagonal
        return True
    
    return False


#   Explicaçõa do "tabuleiro[i][i]":

#   [[0,0],[0,1],[0,2]]
#   [[1,0],[1,1],[1,2]]
#   [[2,0],[2,1],[2,2]]


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

        if tabuleiro[linha][coluna] != " ":                                                 # Se a posição estiver ocupada o sistema avisa e repete para que se escolha nov
            print("Posição já ocupada!")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if vitória(tabuleiro, jogador_atual):                                               # Caso um jogador tenha vencido, o código imprime quem venceu.
            mostrar_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu")
            break

        if jogadas == 9:                                                                    # Caso o número de jogadas chegue a 9 o jogo empata.
            mostrar_tabuleiro(tabuleiro)
            print("Empate")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

jogo()