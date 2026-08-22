for i in range(200,10,-2):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10):
    print(i)

nome = "Indiara"
for i in nome:
    print(i)


controle = 0

while controle < 10:
    somador = int(input("Registro: "))
    controle = controle + somador
    print(f"Vagas disponíveis: {10 - controle}")

print("Oficina lotada!")



print("--- Simulação DO-WHILE (Executa 1ª vez, depois checa) ---")
contador = 0
limite = 5
while True: # Loop infinito garantido para executar pelo menos uma vez
 if contador >= limite:
    break # Ponto de DECISÃO: Se o limite for atingido, usamos 'break' para sair

try:
    print(f"Número {contador + 1} de {limite}:")
    num = float(input("Digite um número: "))

    dobro = num * 2
    triplo = num * 3
    quádruplo = num * 4

    print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")

    contador = contador + 1 # Incremento

except ValueError:
    print("Entrada inválida. Tente novamente.")