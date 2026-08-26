# criando a lista de candidatos
candidatos_validos = []

# loop devalidação e cadastro do candidato
for i in range (5):
    ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
    idade = 2026 - ano_de_nascimento

    # validando         
    if idade < 18:
        print("Candidato não tem idade suficiente")

    # cadastrando
    else:
        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        telefone = input("Digite seu número de telefone: ")

        # adicionando candidato validado a lista
        candidato = {"Nome":nome, "Idade":idade, "Email":email, "Telefone":telefone}
        candidatos_validos.append(candidato)

        # mostrando resultado para o usuário
        print(f"Candidato {nome} cadastrado com sucesso!")
        print(f"{candidatos_validos}")