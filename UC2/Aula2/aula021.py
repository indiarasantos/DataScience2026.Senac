import pandas as pd
import numpy as np
import openpyxl

### LEITURA ARQUIVOS XLSX
# variável      # comando      # caminho arquivo  # argumentos leitura
df_transacoes = pd.read_excel("base_invest.xlsx",sheet_name='Transacoes')
df_ativo = pd.read_excel("base_invest.xlsx",sheet_name='Ativo')

df_compra = df_transacoes[df_transacoes['operacao'] == 'compra']
df_venda = df_transacoes[df_transacoes['operacao'] == 'venda']


max_compra = df_compra['preco'].max()
min_compra = df_compra['preco'].min()
max_venda = df_venda['preco'].max()
min_venda = df_venda['preco'].min()

print(f"Máxima de compra: {max_compra}")
print(f"Mínima de compra: {min_compra}")
print(f"Máxima de venda: {max_venda}")
print(f"Mínima de venda: {min_venda}")

df_transacoes['valor_total'] = df_transacoes['quantidade'] * df_transacoes['preco']

valor_por_ativo = df_transacoes.groupby('id_ativo')['valor_total'].sum()

id_ativo_maior_valor = valor_por_ativo.idxmax()

cnpj_maior_ativo = df_ativo[df_ativo['id_ativo'] == id_ativo_maior_valor]['cnpj'].iloc[0]

print(f"CNPJ com ativo de maior valor: {cnpj_maior_ativo}")