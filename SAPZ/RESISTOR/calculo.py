
cores1 = {
    "preto": 0, 
    "marrom": 1, 
    "vermelho": 2, 
    "laranja": 3, 
    "amarelo": 4, 
    "verde": 5, 
    "azul": 6, 
    "violeta": 7, 
    "cinza": 8, 
    "branco": 9
    }

cores2 = {    
    "marrom": 1,
    "vermelho": 2,
    "verde": 0.5,
    "azul": 0.25,
    "violeta": 0.1,
    "cinza": 0.05,
    "ouro": 5,
    "prata": 10
    }


cor1 = str(input("Cor da primeria listra: ")).lower()
cor2 = str(input("Cor da segunda listra: ")).lower()
cor3 = str(input("Cor da terceira listra: ")).lower()
cor4 = str(input("Cor da quarta listra: ")).lower()

resistencia = ((cores1[cor1]*10)+cores1[cor2])*(10**cores1[cor3])
tolerancia = cores2[cor4]

t_minima = resistencia * (1 - tolerancia / 100)
t_maxima = resistencia * (1 + tolerancia / 100)

print(f'{resistencia} Ω')
print(f'valor maximo: {t_maxima} Ω')
print(f'valor minimo: {t_minima} Ω')