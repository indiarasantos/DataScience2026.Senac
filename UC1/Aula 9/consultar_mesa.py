# dados para testes
mesas_sistema = [
    {
        "numero": 1,
        "status": "ocupada",
        "garcom": "Carlos",
        "pedidos": ["Pizza Margherita", "Suco de Laranja"]
    },
    {
        "numero": 2,
        "status": "livre",
        "garcom": None,
        "pedidos": []
    },
    {
        "numero": 3,
        "status": "ocupada",
        "garcom": "Fernanda",
        "pedidos": []
    },
    {
        "numero": 4,
        "status": "ocupada",
        "garcom": "João",
        "pedidos": ["Feijoada", "Caipirinha"]
    }
]

def consultar_mesa():
    '''
    Função para consultar o status de uma mesa específica, incluindo o garçom vinculado e os pedidos associados.
    Retorna uma lista de pedidos se a mesa estiver ocupada e tiver pedidos registrados.
    '''

    numero_mesa = int(input("Digite o número da mesa que deseja consultar: "))

    mesa_encontrada = None
    # iterando por cada dicionário na lista
    for mesa in mesas_sistema:
        if mesa["numero"] == numero_mesa:
            mesa_encontrada = mesa
            break

    # verificando se a mesa existe
    if mesa_encontrada is None:
        print(f"Mesa {numero_mesa} não encontrada no sistema.")
        return None

    # verificando se está livre
    if mesa_encontrada["status"] != "ocupada":
        print(f"Mesa {mesa_encontrada['numero']} não está ocupada. Status atual: {mesa_encontrada['status']}")
        return None

    # verificando se possui garçom
    if mesa_encontrada["garcom"] is None:
        print(f"Não há garçom cadastrado para a mesa {mesa_encontrada['numero']}.")
        return None

    # verificando os pedidos da mesa, caso houver
    pedidos_da_mesa = mesa_encontrada["pedidos"]
    if not pedidos_da_mesa:
        print(f"Mesa {mesa_encontrada['numero']} atendida por {mesa_encontrada['garcom']}, mas ainda sem pedido registrado.")
        return None

    print(f"Mesa {mesa_encontrada['numero']} pronta: Pedido de atendente {mesa_encontrada['garcom']} encaminhado para cozinha.")
    return pedidos_da_mesa

# chamando a função
consulta = consultar_mesa()
print(consulta)
