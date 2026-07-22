def linhas():
    """Cria uma linha +-----+"""
    print(f"+{largura*'-'}+")

def colunas():
    """Cria duas colunas com uma palavra no centro | palavra |"""
    for linha in range(altura):
        if linha == altura // 2:
            print(f"|{palavra.center(largura)}|")
        else:
            print(f"|{largura*" "}|")

def adicionar_filme():
    """Adiciona filmes ao Arq_Filmes.txt com todas as suas informações"""
    while True:
            
            titulo = input("Digite o título do filme: ")

            if titulo == "":
                break

            ano = input("Digite o ano em que o filme foi lançado: ")
            diretor = input("Digite o nome do diretor: ")
            genero = input("Digite o gênero do filme: ")
            tempo = input("Digite quantos minutos de duração tem o filme: ")

            with open("Arq_Filmes.txt", "a", encoding="utf-8") as f:
                f.write(f"{titulo} - {ano} - {diretor} - {genero} - {tempo}\n")

    print("Filme adicionado com sucesso!")

def quantidade_de_filmes():
        """Conta e imprime a quantidade de filmes presentes no arquivo."""
        with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
            quantidade = len(f.readlines())
            print(f"Quantidade de filmes: {quantidade}")

def informacao_filme():
    """Imprime todas as principais informações dos filmes arquivados."""
    titulo_procurado = input("Digite o titulo do filme: ")

    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
        encontrado = False

        for linha in f:
            dados = linha.strip().split(" - ")

            if dados[0].lower() == titulo_procurado.lower():
                print(f"Título: {dados[0]}")
                print(f"Ano: {dados[1]}")
                print(f"Diretor: {dados[2]}")
                print(f"Gênero: {dados[3]}")
                print(f"Duração: {dados[4]} minutos")
                encontrado = True
                break

        if not encontrado:
            print("Filme não encontrado.")

def ano_filmes():
    """Imprime todos os filmes arquivados dirigidos pelo diretor escolhido."""
    ano_procurado = input("Digite o ano de lançamento do filme: ")
    
    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
        encontrado = False
    
        for linha in f:
            dados = linha.strip().split(" - ")
    
            if dados[1].lower() == ano_procurado.lower():
                print(f"Título: {dados[0]}")
                encontrado = True
                
        if not encontrado:
                print("Nenhum filme encontrado neste ano.")

def diretor_filme():
    """Imprime todos os filmes arquivados dirigidos pelo diretor escolhido."""
    diretor_procurado = input("Digite o diretor do filme: ")

    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
        encontrado = False

        for linha in f:
            dados = linha.strip().split(" - ")

            if dados[2].lower() == diretor_procurado.lower():
                print(f"Título: {dados[0]}")
                encontrado = True
            
        if not encontrado:
                print("Nenhum filme encontrado no nome desse diretor.")
                
def genero_filme():
    """Imprime todos os filmes arquivados que pertençam ao gênero escolhido."""
    genero_procurado = input("Digite o gênero do filme: ")

    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
        encontrado = False

        for linha in f:
            dados = linha.strip().split(" - ")

            if dados[3].lower() == genero_procurado.lower():
                print(f"Título: {dados[0]}")
                encontrado = True

        if not encontrado:
                print("Nenhum filme encontrado com esse gênero.")

def media_filmes():
    """Calcula a média de duração em minutos de todos os filmes arquivados."""
    soma_duracao = 0
    quantidade = 0

    with open("Arq_Filmes.txt", "r", encoding="utf-8") as f:
        for linha in f:
            dados =linha.strip().split(" - ")

            duracao = int(dados[4])
            soma_duracao += duracao
            quantidade += 1

        if quantidade > 0:
            media = soma_duracao / quantidade
            print(f"A média de duração dos filmes é de {media:.2f} minutos.")
        else:
            print("Não existem filmes arquivados.")

altura = 1
largura = 40

palavras = ("Adicionar Filme - 0", "Quantidade total de filmes - 1", "Informações de um filme pelo titulo - 2", "Filmes de um ano específico - 3", "Filmes de um diretor específico - 4", "Filmes de um gênero específico - 5", "Média de duração dos filmes - 6", "Sair - 7")

if __name__ == "__main__":

    for palavra in palavras:
        linhas()
        colunas()
    linhas()

while True:

    try:
        opcao = int(input("O que você deseja fazer: "))
    except ValueError:
        print("Digite apenas um dos números indicados!")
        continue

    if opcao == 0:
        adicionar_filme()
    elif  opcao == 1:
        quantidade_de_filmes()
    elif opcao == 2:
        informacao_filme()
    elif opcao == 3:
        ano_filmes()
    elif opcao == 4:
        diretor_filme()
    elif opcao == 5:
        genero_filme()
    elif opcao == 6:
        media_filmes()
    elif opcao == 7:
        break
    else:
        print("Cáracter inválido: Tente Novamente")