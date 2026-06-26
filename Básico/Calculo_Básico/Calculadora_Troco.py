#Calculadora de troco

valorT = float(input("Qual foi o valor que você etregou para o vendedor?"))
valorP = float(input("Qual o valor que você deveria pagar pelo produto?"))

troco = valorT - valorP

print(f'O valor que você deverá receber de troco será de {troco} reais.')