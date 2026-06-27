sala = {}
n_alunos = int(input("Número de alunos na sala: "))
soma = 0

print()

for i in range(n_alunos):
  nome = input("Nome do aluno: ")
  nota = float(input("Nota do aluno: "))
  sala[nome] = nota

print()

for nome, nota in sala.items():
  print(f'Aluno: {nome} - Nota: {nota}')
  soma = soma + nota
media = soma / len(sala)

print()

print(f'A média da turma é: {media:.1f}')