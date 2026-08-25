# recebendo as medidas da cozinha do usuário
comprimento = float(input("Comprimento da cozinha: "))
largura = float(input("Largura da cozinha: "))
altura = float(input("Altura da cozinha: "))

# calculando a dimensão da área
dimensao = (2 * comprimento * altura) + (2 * largura * altura)

# calculando quantidade de caixas
caixas = dimensao / 1.5

# imprimindo a quantidade para o usuario
print(f"Você vai precisar de {int(caixas)} caixas de azulejos.")