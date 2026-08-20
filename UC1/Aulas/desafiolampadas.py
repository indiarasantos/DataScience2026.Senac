# variavel dos watts
POTENCIA = 3

# pedindo as informações ao usuário
largura = float(input("Largura do cômodo: "))
comprimento = float(input("Comprimento do cômodo: "))

# calculando a dimensão do cômodo
DIMENSAO = int(largura * comprimento)

# conferindo se a lâmpada possui a potência mínima adequada 
if POTENCIA < 3:
    print("A lâmpada não tem potência o suficiente")
# verificando quantidade de lâmpada de acordo com tamanho do cômodo
elif DIMENSAO >= 3 and DIMENSAO <= 5:
    lampadas = 1
    print(f"Você vai precisar de {int(lampadas)} lâmpadas para iluminar este cômodo.")
elif DIMENSAO > 5:
    lampadas = (DIMENSAO/3)
    print(f"Você vai precisar de {int(lampadas)} lâmpadas para iluminar este cômodo.")
# resultado caso o cômodo não tiver o tamanho mínimo indicado para possuir bocal
else:
    print(f"Seu cômodo não possui bocal.")

