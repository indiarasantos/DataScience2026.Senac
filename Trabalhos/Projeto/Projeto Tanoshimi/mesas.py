'''
mesas.py - Tanoshimi - Sistema de Atendimento
Módulo 02: Ocupação e responsabilidade das mesas.
Status possíveis: "livres", "ocupada", "reservada", "em_pagamento".
'''

mesas_sistema = []

def cadastrar_mesa(numero_mesa, capacidade):
    '''
    Registra uma mesa e sua capacidade de atendimento.
    '''

    if not isinstance(numero_mesa, int) or numero_mesa <= 0:
        raise ValueError("Erro: Número da mesa deve ser um inteiro positivo.")
    if not isinstance(capacidade, int) or capacidade <= 0:
        raise ValueError("Erro: Capacidade da mesa deve ser um inteiro positivo.")
    if any(m["numero_mesa"] == numero_mesa for m in mesas_sistema):
        raise ValueError(f"Erro: Mesa {numero_mesa} já cadastrada.")

    mesa = {
        "numero_mesa": numero_mesa,
        "capacidade": capacidade,
        "satatus": "livre",
        "garcom": None,
    }
    mesas_sistema.append(mesa)
    return mesa

def consultar_mesa(numero_mesa, pedidos):
    '''
    Consulta os dados e a situação atual de uma mesa: confirma se está
    ocupada, se já tem garçom vinculado e se já tem pedido registrado —
    e sinaliza o encaminhamento para a cozinha quando os três estiverem ok.
    '''

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
    

    from pedidos import listar_pedidos_da_mesa
    pedidos_da_mesa = listar_pedidos_da_mesa(numero_mesa, pedidos, exibir=False)

    if not pedidos_da_mesa:
        print(f"Mesa {numero_mesa} atendida por {mesa['garcom']}, mas ainda sem pedido registrado.")
    return None
 
    print(f"Mesa {numero_mesa} pronta: pedido de {mesa['garcom']} encaminhado para a cozinha.")
    return pedidos_da_mesa
 
def listar_mesas(status=None):
    """Apresenta mesas livres, ocupadas, reservadas ou em pagamento."""
    if status is None:
        return list(mesas_sistema)
    return [m for m in mesas_sistema if m["status"] == status]
 
def alterar_status_mesa(numero_mesa, novo_status):
    """Atualiza o estado da mesa ao longo do atendimento."""

    status_validos = {"livre", "ocupada", "reservada", "em_pagamento"}
    if novo_status not in status_validos:
        raise ValueError(f"Status inválido. Use um de: {status_validos}")
 
    mesa = next((m for m in mesas_sistema if m["numero_mesa"] == numero_mesa), None)
    if mesa is None:
        print(f"Mesa {numero_mesa} não encontrada.")
        return None
 
    mesa["status"] = novo_status
    if novo_status == "livre":
        mesa["garcom"] = None
    return mesa
 
 
def vincular_garcom_mesa(numero_mesa, nome_garcom, garcons):
    """Define o profissional responsável pela mesa."""
    
    mesa = next((m for m in mesas_sistema if m["numero_mesa"] == numero_mesa), None)
    if mesa is None:
        return f"Erro: A mesa {numero_mesa} não existe."
 
    nomes_validos = [g["nome"] for g in garcons]
    if nome_garcom not in nomes_validos:
        return f"Erro: O garçom {nome_garcom} não trabalha aqui."
 
    mesa["garcom"] = nome_garcom
    if mesa["status"] == "livre":
        mesa["status"] = "ocupada"
    return f"Sucesso: Garçom {nome_garcom} vinculado à mesa {numero_mesa}."
