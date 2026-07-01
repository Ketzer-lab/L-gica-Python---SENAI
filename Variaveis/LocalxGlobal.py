# Variáveis locais são aquelas que estão dentro de uma função e funciona/criada apenas quando chamada.
# Variáveis Globais são aquelas que estão fora de funções e funcionam do inicio ao fim do sistema.


GLOBAL_VAR = 'valor global'

def exemplo_local():
    # Váriavel local - só existe dentro dessa função.

    local_var = 'valor local'
    print('local_var: ', local_var)

    # Acessar variável global para leitura funciona sem declarar 'global'

    print('GLOBAL_VAR: ', GLOBAL_VAR)

    # Usar um built-in (len)

    print('Built-in len(\'abc\'): ', len('abc'))

def exemplo_modifica():
    # Para modificar a variável global dentro da função, declarar 'global'.
    
    global GLOBAL_VAR
    GLOBAL_VAR = 'novo valor global'
    print('GLOBAL_VAR modificado para: ', GLOBAL_VAR)

print('GLOBAL_VAR (antes): ', GLOBAL_VAR)
exemplo_local()
exemplo_modifica()
print('GLOBAL_VAR (depois): ', GLOBAL_VAR)