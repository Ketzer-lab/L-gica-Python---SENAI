nome = "Jhon Doe"
idade = 28
altura = 178
print(nome)
print(idade)
print(altura)

print(nome+" possui "+str(idade)+" anos de idade"+" e "+str(altura)+" centimetros de altura.")
#ou
print(nome, "possui", idade, "anos de idade e", altura, "centimetros de altura.")

#Ao colocar "" antes e depois de idade eu mando o codigo a escrever exatamente o que está entre "".
#Para adicionar mais textos as 'strings' é necessário usar os comando '+' e 'str'.
#'str' = converção de tipo, necessário ja que "nome" é uma palavra e "idade" é um número, ou seja não se conectam apenas com '+'.
#Não é possivel juntar dados de tipo diferentes, como "idade" e "nome".
#A ',' pode ser usada para facilitar o processo.