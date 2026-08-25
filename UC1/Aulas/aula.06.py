# impares = []
# print(type(impares))
# impares = [3,5,13,27]
# print(impares)
# print(impares[0])
# print(type(impares[0]))
# print(impares[3])
# print(impares[-1])

# lista_01 = [
#     12,
#     "Pedro",
#     12.53343,
#     "[{_{^^()}}]",
#     False,
#     0,
#     [2,4,6,8]
#     ]

# print(lista_01[1], lista_01[2], lista_01[4], lista_01[6][2])

# #condicionais

# lista_02 = ["Marcia"]

# if "Marcia" in lista_02:
#     print(lista_02)

# participantes = ["Isaque", "Luana", "Bianca", "Ana Paula"]



# partic_2 = "Hugo"

# participantes.append(partic_2)
# participantes.insert(2,partic_2)
# print(participantes)
# participantes.pop(1)
# print(participantes)
# participantes.remove("Hugo")
# print(participantes)
# participantes.reverse()
# print(participantes)
# participantes.count("Hugo")
# print(participantes)
# print(participantes)
# participantes.clear()
# print(participantes)

#TUPLAS

# participantes = ("Isaque", "Luana", "Fernando", "Bianca", "Ana Paula")
# print(participantes)
# partic_2 = ("Hugo",)
# participantes = participantes + partic_2
# print(participantes)
# participants_02 = ("Fernando", "111.111.******", "Avenida Dr. , 444",)
# print(participants_02.count("Fernando"))
# print(participants_02.index("Avenida Dr. , 444"))
# listinha_partic_02 = list(participants_02)
# print(listinha_partic_02)

# SETS

# numeros_pares = {
#     202,
#     203,
#     204,
#     204,
#     205,
#     219,
#     291,
#     292,
#     202
# }
# print(numeros_pares,type(numeros_pares))

# numeros_impares = {111, 111, 112, 291, 291, 205}
# print(numeros_impares,type(numeros_impares))

# print(numeros_pares.intersection(numeros_impares))

# numeros_pares.remove(205)
# print(numeros_pares,type(numeros_pares))

# DICIONÁRIOS

produtos = {
    "maçã":5.99,
    "laranja":4.79
}

print(produtos,type(produtos))
print(produtos.items())
print(produtos.keys())
print(produtos.values())
print(produtos.get("laranja"))

produtos2 = produtos.copy()
print(produtos2)
#produtos2.pop("maçã")
print(produtos2)
produtos2["maçã"] = 7.99

print(produtos2)

achadinhos = {}
print(type(achadinhos))
achadinhos["capinha celular"] = 12.99
print(achadinhos)