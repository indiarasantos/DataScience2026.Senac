def cadastrar_mesa():
    mesas = {}
    numero_mesa = 0
    quantidade_mesas = int(input("Quantas mesas deseja cadastrar? "))
    for i in range (quantidade_mesas):
        numero_mesa += 1
        capaciade = int(input("Capacidade de atendimento da mesa: "))
        mesas[numero_mesa] = {
            "capaciade": capaciade,
            "status": "Livre",
            "garcom": None,
            "pedido": None
        }
    return mesas


mesas = cadastrar_mesa()
for numero, dados in mesas.items():
    print(f"Mesa {numero}: {dados}")