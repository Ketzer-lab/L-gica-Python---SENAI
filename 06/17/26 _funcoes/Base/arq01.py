# Normalmente colocamos as Funções antes de qualquer coisa, pois caso as variaveis estejam acima, as funções podem não encontar o que esta acima.

def somar_valores(parametro1, parametro2):
    """Docstring: Soma 2 valores. """
    #Corpo da função:
    resultado = parametro1 + parametro2
    return  resultado
soma = somar_valores(2, 3)
print(soma)