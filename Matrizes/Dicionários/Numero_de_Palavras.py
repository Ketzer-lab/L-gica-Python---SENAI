tabela = {}

texto = input("Escreva aqui! ")
palavras = texto.split()   # Divide a frase por palavras

for palavra in palavras:   # para cada palavra na variavel 'palavras'
  if palavra in tabela:    # se a palavra estiver na tabela aumente seu valor em 1
    tabela[palavra] += 1
  else:                    # se a palavra não estiver na tabela, adicione a palavra e iguale seu valor a 1
    tabela[palavra] = 1

print()

for palavra, quantidade in tabela.items():
  print(f'{palavra}: {quantidade}')

dif = len(tabela)
print(f"Existem {dif} palavras diferentes no texto")