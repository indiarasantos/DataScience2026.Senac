def calcular_multa():
    '''
    A função recebe o peso e calcula a multa do pescador
    '''
    multa_pescador_total = 0
    multa_pescador = 0

    while True:
        peso = float(input("Digite o peso do peixe. (Digite 0 para finalizar o programa).: "))
        limite = 100
        
        if peso > limite:
            multa = 4.00
            multa_pescador = (peso - limite) * multa
            print(f"Multa de R$ {multa_pescador:.2f}")
            multa_pescador_total += multa_pescador
        elif peso > 0 and peso <= limite:
            print("Peso dentro do limite. Nenhuma multa a pagar.")
        else:
            break

    print(f"Multa total a pagar: R$ {multa_pescador_total:.2f}")