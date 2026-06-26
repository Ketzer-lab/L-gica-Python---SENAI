#Calculadora de média ponderada

nota1 = float(input("Qual a primeira nota?"))
nota2 = float(input("Qual a segunda nota?"))
nota3 = float(input("Qual a terceira nota?"))

peso1 = float(input("Qual o peso da primeira nota?"))
peso2 = float(input("Qual o peso da segunda nota?"))
peso3 = float(input("Qual o peso da terceira nota?"))

notaF = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3) #Na média ponderada se multiplica a nota do aluno pelo peso da avaliação e divede o resultado pela soma dos pesos.

print(f'A média ponderada final do aluno é {notaF}.')