while True:
            titulo = input("Escreva o título do filme: ")

            if titulo == "":
                break
        
            titulos.append(titulo)

            diretor = input("Escreva o nome do diretor: ")
        
            if diretor == "":
                break

            diretores.append(diretor)

            genero = input("Escreva o gênero do filme: ")

            if genero == "":
                break

            generos.append(genero)

            tempo = input("Escreva quantos minutos de duração tem o filme: ")

            if tempo == "":
                break

            duracao.append(tempo)

        with open("Arq_Filmes.txt", "w") as f:
            for i in range(len(titulos)):
                f.write(f"{titulos[i]} - {diretores[i]} - {generos[i]} - {duracao[i]}\n")

        continue

if  opcao == 1:
        print(len(titulos))
        continue

titulo_procurado = input("Digite o titulo do filme:")

        with open("Arq_Filmes.txt", "r") as f:
            encontrado = False

            for linha in f:
                dados = linha.strip().split(" - ")

            if dados[0].lower() == titulo_procurado.lower():
                print(f"Título: {dados[0]}")
                print(f"Diretor: {dados[1]}")
                print(f"Gênero: {dados[2]}")
                print(f"Duração: {dados[3]} minutos")
                encontrado = True
                break

        if not encontrado:
            print("Filme não encontrado.")

        continue