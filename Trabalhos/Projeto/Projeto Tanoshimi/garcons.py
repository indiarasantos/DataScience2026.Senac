"""
garcons.py — Tanoshimi · Sistema de Atendimento
Módulo 03: Equipe de atendimento.
"""
 
garcons_sistema = []
 
 
def cadastrar_garcom(matricula, nome):
    """Registra nome, matrícula e situação profissional."""
    if any(g["matricula"] == matricula for g in garcons_sistema):
        raise ValueError(f"Matrícula {matricula} já cadastrada.")
 
    garcom = {"matricula": matricula, "nome": nome.strip(), "status": "disponivel"}
    garcons_sistema.append(garcom)
    return garcom
 
 
def consultar_garcom(matricula):
    """Localiza o cadastro por meio da matrícula."""
    return next((g for g in garcons_sistema if g["matricula"] == matricula), None)
 
 
def listar_garcons(apenas_ativos=False):
    """Lista profissionais ativos e seus atendimentos."""
    if apenas_ativos:
        return [g for g in garcons_sistema if g["status"] != "folga"]
    return list(garcons_sistema)
 
 
def alterar_status_garcom(matricula, novo_status):
    """Atualiza disponibilidade, atendimento ou encerramento do turno."""
    status_validos = {"disponivel", "em_atendimento", "folga"}
    if novo_status not in status_validos:
        raise ValueError(f"Status inválido. Use um de: {status_validos}")
 
    garcom = consultar_garcom(matricula)
    if garcom is None:
        print(f"Garçom {matricula} não encontrado.")
        return None
    garcom["status"] = novo_status
    return garcom
 
 
def listar_mesas_do_garcom(nome_garcom, mesas):
    """Mostra as mesas atribuídas a um profissional."""
    return [m["numero_mesa"] for m in mesas if m.get("garcom") == nome_garcom]