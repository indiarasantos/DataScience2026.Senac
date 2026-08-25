# Recebendo números do usuário já convertidos para inteiros
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))

#  Encontrando o maior número
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

# Encontrando o menor número
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

# Encontrando número do meio
meio = (n1 + n2 + n3) - (maior + menor)


# Mostrando resultado ao usuário
print(f"Números ordenados: {menor}, {meio}, {maior}")