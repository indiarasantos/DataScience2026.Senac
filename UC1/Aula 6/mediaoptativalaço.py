# definindo a variável de ajuste da nota optativa
ajuste_nota = 0

# criando lista vazia com resultados de alunos
resultados = []

for i in range (5):
# pedindo as notas para o usuário
    nome_estudante = input("Digite o nome do estudante: ")
    nota_normal01 = float(input("Insira a nota da primeira avaliação: "))
    nota_normal02 = float(input("Insira a nota da segunda avaliação: "))
    nota_optativa = float(input("Insira a nota da avaliação optativa: "))

    # calculando a média ponderada das notas
    if nota_optativa == 0:
        ajuste_nota = -1
    else:
        nota_optativa = nota_optativa

    if nota_normal01 >= nota_normal02 and nota_normal02 < nota_optativa:
        nota_normal02 = nota_optativa
    elif nota_normal02 >= nota_normal01 and nota_normal01 < nota_optativa:
        nota_normal01 = nota_optativa
    else:
        nota_normal01 = nota_normal01
        nota_normal02 = nota_normal02

    media = (nota_normal01 + nota_normal02 + ajuste_nota) / 2

    # definindo a situação do aluno com base na média
    if media >= 6.0:
        situacao = "Aprovado"
    elif media >= 3.0 and media < 6.0:
        situacao = "Em recuperação"
    else:
        situacao = "Reprovado"

    resultados.append(f"{nome_estudante} - {situacao}")
        
    # mostrando a média e a situação do aluno
    print(resultados)