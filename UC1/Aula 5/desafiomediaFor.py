# Programa para calculo de média do estudante
print("====== MÉDIA DO ESTUDANTE ======")

estudantes = []

for i in range (10):
    # Recebendo notas do usuário já convertidas para float
    nome_estudante = input("Digite o nome do estudante: ")
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    nota_3 = float(input("Digite a terceira nota: "))
    nota_4 = float(input("Digite a quarta nota: "))

    # Calculando a média do estudante
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

    # Encontrando a situação do estudante
    if media > 7:
        situacao = "Aprovado"
    elif media >= 5 and media <= 7:
        situacao = "Em recuperação"
    else:
        situacao = "Reprovado"

    estudantes.append(f"{nome_estudante} - {situacao} com média {media:.1f}")

    # Mostrando resultado para usuário
    print(f"Estudante {nome_estudante} {situacao}, com média {media:.1f}!")
    print(f"{estudantes}")