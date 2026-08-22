acertou = 0

while acertou < 5:
    print(f"Número {contador + 1} de {limite}:")
    num = float(input("Digite um número: "))
    
    dobro = num * 2
    triplo = num * 3
    quádruplo = num * 4
    
    print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
    
    contador = contador + 1 # IMPORTANTÍSSIMO! Incrementa o contador para evitar loo