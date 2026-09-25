def consultar_mesa(numero_mesa, pedidos):
    """
    Consulta os dados e a situação atual de uma mesa: confirma se está
    ocupada, se já tem garçom vinculado e se já tem pedido registrado —
    e sinaliza o encaminhamento para a cozinha quando os três estiverem ok.
    Esta é a função que você (Indi) ficou responsável por implementar.
    """
    mesa = next((m for m in mesas_sistema if m["numero_mesa"] == numero_mesa), None)
    if mesa is None:
        print(f"Mesa {numero_mesa} não encontrada.")
        return None
 
    if mesa["status"] != "ocupada":
        print(f"Mesa {numero_mesa} não está ocupada. Status atual: {mesa['status']}")
        return None
 
    if mesa["garcom"] is None:
        print(f"Mesa {numero_mesa} ocupada, mas sem garçom vinculado.")
        return None
 
    import listar_pedidos_da_mesa
    pedidos_da_mesa = listar_pedidos_da_mesa(numero_mesa, pedidos, exibir=False)
    if not pedidos_da_mesa:
        print(f"Mesa {numero_mesa} atendida por {mesa['garcom']}, mas ainda sem pedido registrado.")
        return None
 
    print(f"Mesa {numero_mesa} pronta: pedido de {mesa['garcom']} encaminhado para a cozinha.")
    return pedidos_da_mesa

consulta = consultar_mesa()