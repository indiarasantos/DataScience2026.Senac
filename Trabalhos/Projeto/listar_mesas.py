mesas_sistema_alterada = [  
    {"numero_mesa": 1, "capacidade": 2, "status": "ocupada"},  
    {"numero_mesa": 2, "capacidade": 2, "status": "livre"},  
    {"numero_mesa": 3, "capacidade": 2, "status": "livre"},  
    {"numero_mesa": 4, "capacidade": 4, "status": "livre"},  
    {"numero_mesa": 5, "capacidade": 4, "status": "livre"},  
    {"numero_mesa": 6, "capacidade": 4, "status": "livre"},  
    {"numero_mesa": 7, "capacidade": 8, "status": "ocupada"},  
    {"numero_mesa": 8, "capacidade": 8, "status": "ocupada"},  
    {"numero_mesa": 9, "capacidade": 8, "status": "ocupada"},  
]  
  
mesas_sistema = [  
    {"numero_mesa": 1, "capacidade": 2, "status": "livre"},  
    {"numero_mesa": 2, "capacidade": 2, "status": "livre"},  
    {"numero_mesa": 3, "capacidade": 2, "status": "livre"},  
    {"numero_mesa": 4, "capacidade": 4, "status": "livre"},  
    {"numero_mesa": 5, "capacidade": 4, "status": "livre"},  
    {"numero_mesa": 6, "capacidade": 4, "status": "livre"},  
    {"numero_mesa": 7, "capacidade": 8, "status": "livre"},  
    {"numero_mesa": 8, "capacidade": 8, "status": "livre"},  
    {"numero_mesa": 9, "capacidade": 8, "status": "livre"},  
]  
  
def listar_mesas(mesas=None):  
    # Caso o parâmetro mesas seja None (não foi mandado), utiliza a lista padrão do sistema  
    if mesas is None:  
        mesas = mesas_sistema  
  
    if not isinstance(mesas, list):  
        print("Erro! O valor passado não é uma lista.")  
        return []  
  
    if not mesas:  
        print("Nenhuma mesa cadastrada no sistema.")  
        return []  
  
    # Interação com o usuário, para dar mais frufruzera ao código  
    print("\n======================================")  
    print("          SISTEMA DE MESAS")  
    print("======================================")  
    print(f"Total de mesas: {len(mesas)}")  
  
    print("\n--- TODAS AS MESAS ---")  
  
    for mesa in mesas:  
        print(  
            f"Mesa {mesa['numero_mesa']} | "  
            f"Capacidade: {mesa['capacidade']} | "  
            f"Status: {mesa['status']}"  
        )  
  
    ## o alterar_status_mesa() precisa continuar conseguindo enxergar a mesa 1, mesmo ela estando indisponível.  
    return mesas 
 

def listar_pedidos_da_mesa(numero_mesa: int, pedidos: list[dict], status: str | None = None, exibir: bool = True) -> list[dict]:
    '''
    Apresenta e retorna todos os pedidos associados a uma mesa e, opcionalmente, apresenta-os no terminal.

    Args:
        numero_mesa: Número identificador da mesa.
        pedidos: Lista de dicionários representando os pedidos.
        status: Status opcional usado para filtrar os pedidos.
        exibir: Indica se os pedidos encontrados devem ser exibidos no terminal. O padrão é True.

    Returns:
        Lista de pedidos associados à mesa e ao status informado.
        Retorna uma lista vazia quando nenhum pedido é encontrado.

    Raises:
        TypeError: Se os parâmetros tiverem tipos inadequados.
        ValueError: Se o número da mesa não for maior que zero.
    '''

    LARGURA_EXIBICAO = 100

    # Validações
    if not isinstance(numero_mesa, int):
        raise TypeError(
            "Parâmetro inválido: o número da mesa deve ser um número inteiro.")

    if numero_mesa <= 0:
        raise ValueError(
            "Parâmetro inválido: o número da mesa deve ser maior que zero.")

    if not isinstance(pedidos, list):
        raise TypeError(
            "Parâmetro inválido: os pedidos devem ser fornecidos em uma lista.")

    if status is not None and not isinstance(status, str):
        raise TypeError(
            "Parâmetro inválido: o status deve ser uma string ou None.")

    if not isinstance(exibir, bool):
        raise TypeError(
            "Parâmetro inválido: exibir deve ser um valor booleano.")

    # Lógica da função
    pedidos_da_mesa = []

    for pedido in pedidos:
        if pedido['numero_mesa'] == numero_mesa:

            if status is not None:
                if pedido['status'].lower() == status.lower():
                    pedidos_da_mesa.append(pedido)
            else:
                pedidos_da_mesa.append(pedido)

    if not exibir:
        return pedidos_da_mesa

    # Exibição no terminal
    print("=" * LARGURA_EXIBICAO)
    print("RESTAURANTE TANOSHIMI - VISÃO DO GARÇOM".center(LARGURA_EXIBICAO))
    print("=" * LARGURA_EXIBICAO)

    if status is not None:
        print(
            f"PEDIDOS DA MESA {numero_mesa} - STATUS: {status.upper()}".center(LARGURA_EXIBICAO))
    else:
        print(f"PEDIDOS DA MESA {numero_mesa}".center(LARGURA_EXIBICAO))

    print("=" * LARGURA_EXIBICAO)

    if not pedidos_da_mesa:

        if status is None:
            mensagem = "Nenhum pedido foi encontrado para essa mesa."
        else:
            mensagem = f"Nenhum pedido com status '{status.lower()}' foi encontrado para essa mesa."

        print(mensagem.center(LARGURA_EXIBICAO))

    for indice_pedido, pedido in enumerate(pedidos_da_mesa):
        if indice_pedido != 0:
            print("=" * LARGURA_EXIBICAO)

        print(
            f"PEDIDO {pedido['numero_pedido']} ({pedido['status']})".center(LARGURA_EXIBICAO))
        print("=" * LARGURA_EXIBICAO)

        itens = pedido['itens']

        if itens:
            for indice_item, item in enumerate(itens, start=1):
                codigo_prato = item["codigo_prato"]
                nome_prato = item['nome_prato']
                quantidade = item['quantidade']
                preco_unitario = item["preco_unitario"]
                subtotal = item["subtotal"]
                observacoes = item['observacoes']

                print(
                    f"{indice_item:02d} - {nome_prato:<25} | Qtd: {quantidade} | Unitário: R$ {preco_unitario:>7.2f} | Subtotal: R$ {subtotal:>7.2f}")

                print(" "*5 + f"Código do prato: {codigo_prato}")

                if observacoes:
                    print(" "*5 + f"Observações: {observacoes}")

                if indice_item != len(itens):
                    print("- " * (LARGURA_EXIBICAO // 2))
        else:
            print("Nenhum item foi adicionado ao pedido.".center(LARGURA_EXIBICAO))

    print("=" * LARGURA_EXIBICAO)

    return pedidos_da_mesa

import random

garcoms = [
    "Paulo", "Lucas", "Maria", "Ana", "Luiz",
    "Carolina", "Gabriel", "Fabiana", "Eloan", "Roberta"
]

mesa = [None] * 10


def vincular_garcom_mesa(numero_mesa, nome_garcom):

    if numero_mesa is None or nome_garcom is None:
        return "Erro: Falta enviar o número da mesa ou o nome do garçom."

    if type(numero_mesa) is not int or type(nome_garcom) is not str:
        return "Erro: Mesa deve ser número inteiro e Garçom deve ser texto."

    if numero_mesa < 1 or numero_mesa > len(mesa):
        return f"Erro: A mesa {numero_mesa} não existe no restaurante."

    if nome_garcom not in garcoms:
        return f"Erro: O garçom {nome_garcom} não trabalha aqui."

    posicao_lista = numero_mesa - 1
    mesa[posicao_lista] = nome_garcom

    return f"Sucesso: Garçom {nome_garcom} vinculado à mesa {numero_mesa}."

def consultar_mesa(mesas_sistema_alterada, mesa_garcons, pedidos):
    '''
    Função para consultar o status de uma mesa específica, incluindo o garçom vinculado e os pedidos associados.
    Retorna uma lista de pedidos se a mesa estiver ocupada e tiver pedidos registrados.    
    '''

    numero_mesa = int(input("Digite o número da mesa que deseja consultar: "))

    # Verifica se a mesa existe
    mesa_encontrada = next((m for m in mesas_sistema_alterada if m["mesa"] == numero_mesa), None)

    if mesa_encontrada is None:
        print(f"Mesa {numero_mesa} não encontrada no sistema.")
        return None

    # Verifica se a mesa está ocupada
    if mesa_encontrada["status"] != "ocupada":
        print(f"Mesa {numero_mesa} não está ocupada. Status atual: {mesa_encontrada['status']}")
        return None

    # Verifica se há garçom vinculado
    garcom = mesa_garcons[numero_mesa - 1]
    if garcom is None:
        print(f"Mesa {numero_mesa} ocupada, mas sem garçom vinculado.")
        return None

    # Busca os pedidos da mesa
    pedidos_da_mesa = listar_pedidos_da_mesa(numero_mesa, pedidos, exibir=False)
    if not pedidos_da_mesa:
        print(f"Mesa {numero_mesa} atendida por {garcom}, mas ainda sem pedido registrado.")
        return None

    print(f"Mesa {numero_mesa} pronta: Pedido de atendente {garcom} encaminhado para cozinha.")
    return pedidos_da_mesa
