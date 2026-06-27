pontos = 0
pergunta1 = input("Qual o pokémon inicial de fogo da 5° gen? (A - Tepig / B - Fenikin / C - Chinchar / D - Cindaquil) ")
pergunta2 = input("Qual o nome do protagonista do anime original de Pokémon? (A - Serena / B - Red / C - Ash / D - Satoshi) ")
pergunta3 = input("Quantos pokémons existem nos jogos da 1° gen? (A- 148 / B - 149 / C - 150 / D - 151)" )
pergunta4 = input("Quais foram os primeiros jogos de pokémeon? (A - Black & White / B - Fire Red & Leaf Green / C - Ruby & Saphire / D - Nenhum desses )")

if pergunta1 == 'A':
  pontos = pontos + 1
if pergunta2 == 'D':
  pontos = pontos + 1
if pergunta3 == 'D':
  pontos = pontos + 1
if pergunta4 == 'D':
  pontos = pontos + 1

print(f'Sua pontuação é de {pontos} ponto(s)')