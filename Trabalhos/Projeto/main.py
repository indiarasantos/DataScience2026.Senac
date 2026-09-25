from consultar_mesa import consultar_mesa
from listar_mesas import listar_mesas, mesas_sistema_alterada
from vincular_garcom_mesa import mesa as mesa_garcons
from vincular_garcom_mesa import vincular_garcom_mesa

vincular_garcom_mesa(1, "Paulo")
listar_mesas(mesas_sistema_alterada)
pedidos = [
	{
		"numero_mesa": 1,
		"numero_pedido": 1,
		"status": "aberto",
		"itens": [],
	}
]

consulta = consultar_mesa(mesas_sistema_alterada, mesa_garcons, pedidos)
if consulta:
	print(f"\n{len(consulta)} pedido(s) confirmado(s) para envio à cozinha.")