# definindo variável com preço do combustível
preco_combustivel = 6.15

# pedido os dados ao usuário
km_inicial = float(input("Marcação de km no início do dia: "))
km_final = float(input("Marcação de km ao final do dia: "))
combustivel = float(input("Litros de combustível gasto: "))
valor_recbido = float(input("Valor total recebido: "))

# calculando a media de Km/L
media_consumo = (km_final - km_inicial) / combustivel

# calculando o lucro
lucro = valor_recbido - (combustivel * 6.15)

# imprimindo resultado ao usuário
print(f"Você rodou em média {media_consumo}Km/L e lucrou R$ {lucro:.2f} hoje!")