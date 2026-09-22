import mysql.connector

# 1. conectar banco de dados
conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="meu_ecommerce"
        )

# 2. criar objeto cursor para executar as queries
cursor = conexao.cursor()

# 3. definir query
query_produtos = "SELECT * FROM Produtos"

# 4. executar query
cursor.execute(query_produtos)

# 5. obter os resultados
resultados = cursor.fetchall()
print(resultados)

# 6. exibir os resultados
print(resultados) # sem quebra de linha

for linha in resultados: # com quebra de linha
    print(linha)

# 7. fechar conexão
cursor.close()
conexao.close()