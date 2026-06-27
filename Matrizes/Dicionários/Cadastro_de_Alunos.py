# CADASTRO DE ALUNOS E NOTAS

sala = {}
n_alunos = int(input("Número de alunos na sala: "))

print()

for i in range(n_alunos):
  nome = input("Nome do aluno: ")
  nota = float(input("Nota do aluno: "))
  sala[nome] = nota

print()

for nome, nota in sala.items():
  print(f'Aluno: {nome} - Nota: {nota}')

media = sum(sala.values()) / len(sala)

print()

print(f'A média da turma é: {media}')