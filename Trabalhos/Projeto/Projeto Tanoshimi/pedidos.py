"""
pedidos.py — Tanoshimi · Sistema de Atendimento
Módulo 04: Núcleo das operações.
Status possíveis: "aberto", "em_preparo", "pronto", "entregue", "pago", "cancelado".
"""
 
pedidos_sistema = []
 
 
def criar_pedido(numero_mesa, nome_garcom):
    """Abre o pedido e associa mesa e responsável."""
    from pagamentos import gerar_numero_pedido
 
    pedido = {
        "numero_pedido": gerar_numero_pedido(),
        "numero_mesa": numero_mesa,
        "garcom": nome_garcom,
        "itens": [],
        "status": "aberto",
    }
    pedidos_sistema.append(pedido)
    return pedido
 
 
def adicionar_item_pedido(numero_pedido, codigo_prato, nome_prato, quantidade, preco_unitario, observacoes=""):
    """Inclui prato, quantidade e observações no pedido."""
    pedido = consultar_pedido(numero_pedido)
    if pedido is None:
        print(f"Pedido {numero_pedido} não encontrado.")
        return None
 
    item = {
        "codigo_prato": codigo_prato,
        "nome_prato": nome_prato,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "subtotal": round(quantidade * preco_unitario, 2),
        "observacoes": observacoes,
    }
    pedido["itens"].append(item)
    return pedido
 
 
def remover_item_pedido(numero_pedido, codigo_prato, quantidade=None):
    """Remove um item ou reduz sua quantidade."""
    pedido = consultar_pedido(numero_pedido)
    if pedido is None:
        return None
 
    for item in pedido["itens"]:
        if item["codigo_prato"] == codigo_prato:
            if quantidade is None or quantidade >= item["quantidade"]:
                pedido["itens"].remove(item)
            else:
                item["quantidade"] -= quantidade
                item["subtotal"] = round(item["quantidade"] * item["preco_unitario"], 2)
            return pedido
 
    print(f"Item {codigo_prato} não encontrado no pedido {numero_pedido}.")
    return None
 
 
def consultar_pedido(numero_pedido):
    """Busca o registro pelo número do pedido."""
    return next((p for p in pedidos_sistema if p["numero_pedido"] == numero_pedido), None)
 
 
def calcular_total_pedido(numero_pedido):
    """Soma os itens considerando quantidades e preços."""
    pedido = consultar_pedido(numero_pedido)
    if pedido is None:
        return 0.0
    return round(sum(item["subtotal"] for item in pedido["itens"]), 2)
 
 
def alterar_status_pedido(numero_pedido, novo_status):
    """Controla aberto, preparo, pronto, entregue e pago."""
    status_validos = {"aberto", "em_preparo", "pronto", "entregue", "pago", "cancelado"}
    if novo_status not in status_validos:
        raise ValueError(f"Status inválido. Use um de: {status_validos}")
 
    pedido = consultar_pedido(numero_pedido)
    if pedido is None:
        print(f"Pedido {numero_pedido} não encontrado.")
        return None
    pedido["status"] = novo_status
    return pedido
 
 
def cancelar_pedido(numero_pedido, motivo, responsavel):
    """Cancela o pedido e registra motivo e responsável."""
    pedido = consultar_pedido(numero_pedido)
    if pedido is None:
        return None
    pedido["status"] = "cancelado"
    pedido["cancelamento"] = {"motivo": motivo, "responsavel": responsavel}
    return pedido
 
 
def listar_pedidos_da_mesa(numero_mesa, pedidos, status=None, exibir=True):
    """Apresenta e retorna o consumo (pedidos) relacionado à mesa."""
    if not isinstance(numero_mesa, int):
        raise TypeError("numero_mesa deve ser um número inteiro.")
    if numero_mesa <= 0:
        raise ValueError("numero_mesa deve ser maior que zero.")
    if not isinstance(pedidos, list):
        raise TypeError("pedidos deve ser fornecido em uma lista.")
 
    resultado = [
        p for p in pedidos
        if p["numero_mesa"] == numero_mesa and (status is None or p["status"] == status)
    ]
 
    if exibir:
        print(f"Mesa {numero_mesa}: {len(resultado)} pedido(s) encontrado(s).")
 
    return resultado