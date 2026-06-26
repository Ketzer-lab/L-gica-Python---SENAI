#Calculadora de Baskhara

A = float(input("Qual o número A?"))
B = float(input("Qual o número B?"))
C = float(input("Qual o número C?"))

delta = float((B**2 - 4*A*C)**0.5)
baskhara1 = (-B + (delta))/(A*2)
baskhara2 = (-B - (delta))/(A*2)

print(f'A primeira raiz da equação é {baskhara1} e a sugunda raiz é {baskhara2}.')