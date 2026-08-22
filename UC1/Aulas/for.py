for i in range(5):
    try:
        print(f"Número {i + 1} de 5:")
        num = float(input("Digite um número: "))
        
        dobro = num * 2
        triplo = num * 3
        quádruplo = num * 4
        
        print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
    except ValueError:
        print("Entrada inválida. Tente novamente.")