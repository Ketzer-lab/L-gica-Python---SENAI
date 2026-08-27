notas = []
for i in range(4):
    while True:
        try:
            valor = float(input(f'Digite a nota {i+1}: '))
            if valor < 0 or valor > 10:
                print("Informe a nota entre 0 e 10.")
                continue
            notas.append(valor)
            break
        except Exception:
            print("Entradaninvalida. Digite um número.")

media = sum(notas) / 4
status = ""
if media < 5:
    status = "Reprovado"
elif 5 < media < 7:
    status = "Exame"
else:
    status = "Aprovado"

print(f'Média: {media:.2f} - {status}!')