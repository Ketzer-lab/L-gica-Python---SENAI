soma = 0
while True:
  valor = int(input("Digite um número (0 para sair): "))
  if valor == 0:
    break                                                           # O comando 'break' serve para parar aquela parte do código.
  soma += valor

print(f'Soma: {soma}')