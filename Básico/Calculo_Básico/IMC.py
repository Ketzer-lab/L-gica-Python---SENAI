#Calculadora de imc

altura = float(input("Qual a sua altura?"))
massa = float(input("Qual a sua massa (peso)?"))
imc = float(massa/(altura**2))

print(f'O seu índicie de massa corporea(imc) é {imc}.')

#Potenciação em Python se escreve com '**' seguido pelo número desejado, como por exemplo, se eu quiser um número ao quadrado eu escrevo o número e depois '**2'.