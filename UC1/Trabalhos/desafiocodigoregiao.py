# pedindo o codigo para o usuário
codigo = int(input("Digite o codigo do produto: "))

# usando match case para verificar o código e imprimir a região correspondente
match codigo:
    case 1:
        print("Sul")
    case 2:
        print("Norte")
    case 3:
        print("Leste")
    case 4:
        print("Oeste")
    case 5 | 6:
        print("Nordeste")
    case 7 | 8 | 9:
        print("Sudeste")
    case 10:
        print("Centro-Oeste")
    case 11:
        print("Noroeste")
    case _:
        print("Importado")