pontos = 0
resposta1 = input("Questão 1 (A/B/C/D) ")
resposta2 = input("Questão 2 (A/B/C/D) ")
resposta3 = input("Questão 3 (A/B/C/D) ")
if resposta1 == 'B':
  pontos = pontos + 1

if resposta2 == 'A':
  pontos = pontos + 1

if resposta3 == 'D':
  pontos = pontos + 1

print(f'Pontuação:{pontos}')