'''
cardapio.py - Tanoshimi - Sistema de Atendimento
Módulo 01: Gestão da oferta de pratos
'''
cardapio_sistema = []
_proximo_codigo = 1

def cadastrar_prato(nome, descricao, preco, categoria, disponivel=True):
    ''' Cadastra nome, descrição, preço, categoria e disponibilidade do prato.
    '''

    global _proximo_codigo

    if not isintance(nome, str) or not nome.strip():
        raise ValueError("Erro: Nome do prato é obrigatório.")
    if not isintance(preco, (int,float)) or preco <= 0:
        raise ValueError("Erro: Preço deve ser um número maior que zero.")
    if not isinstance(categoria, str) or not categoria.strip():
        raise ValueError("Categoria é obrigatória.")


    prato = {
        "codigo": _proximo_codigo,
        "nome": nome.strip(),
        "descricao": (descricao or "").strip(),
        "preco": float(preco),
        "categoria": categoria.strip(),
        "disponivel": bool(disponivel),
    }
    cardapio_sistema.append(prato)
    _proximo_codigo += 1
    return prato

def consultar_prato(codigo=None, nome=None):
    '''
    Localiza um prato pelo código ou nome.
    '''

    if codigo is None and nome is None:
        raise ValueError("Informe o código ou o nome do prato.")

    for prato in cardapio_sistema:
        if codigo is not None and prato["codigo"] == codigo:
            return prato
        if nome is not None and prato["nome"].lower() == nome.strip().lower():
            return prato
    return None

def listar_cardapio(apenas_disponiveis=True):
    '''
    Retorna os pratos disponíveis para o usuário.
    '''
    if apenas_disponiveis:
        return [p for p in cardapio_sistema if p ["disponivel"]]

    return list(cardapio_sistema)

def atualizar_prato(codigo, **campos):
    '''
    Altera os dados do prato.
    '''

    prato = consultar_prato(codigo=codigo)
    if prato is None:
        print(f"Prato {codigo} não encontrado.")
        return None

    campos_validos = {"nome", "descricao", "preco", "categoria"}

    for chave, valor in campos.items():
        if chave in campos_validos:
            parto[chave] = valor
        return prato

def alterar_disponibilidade_prato(codigo, disponivel):
    '''
    Ativa ou desativa um item sem precisar excluir o cadastro.
    '''

    prato = consultar_prato(codigo=codigo)
    if prato is None:
        print(f"Prato {codigo} não encontrado.")
        return none
    prato["disponivel"] = bool(disponivel)
    return prato    

