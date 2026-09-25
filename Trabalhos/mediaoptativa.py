# pedindo as notas para o usuário
nota_normal01 = float(input("Insira a nota da primeira avaliação: "))
nota_normal02 = float(input("Insira a nota da segunda avaliação: "))
nota_optativa = float(input("Insira a nota da avaliação optativa: "))

# definindo a variável de ajuste da nota optativa
ajuste_nota = 0

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
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# mostrando a média e a situação do aluno
print(f"A média do aluno é: {media:.1f}")
print(f"Situação: {situacao}")