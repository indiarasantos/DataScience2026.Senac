# criando a lista de candidatos
candidatos = []

# loop de validação e cadastro do candidato
for i in range (13):
    ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
    permissao = 2026 - ano_de_nascimento

    # validando       
    if permissao < 18:
        print("Candidato não tem idade suficiente")

    # cadastrando
    else:
        nome = input("Digite seu nome: ")
        telefone = input("Digite seu número de telefone: ")
        email = input("Digite seu e-mail: ")

        # adicionando candidato validado a lista
        candidatos.append(f"({nome} - {permissao} anos)")

        # mostrando resultado para o usuário
        print(f"Candidato {nome} cadastrado com sucesso!")
        print(f"{candidatos}")