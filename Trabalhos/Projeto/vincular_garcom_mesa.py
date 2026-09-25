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