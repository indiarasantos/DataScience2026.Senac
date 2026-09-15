import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# dados exemplo
dados = np.array([12,15,17,20,22,25,28,30,35,40])
print(dados)

#calculando os quartis
q1 = np.percentile(dados,25)
q2 = np.percentile(dados,50)
q3 = np.percentile(dados,75)

print("Primeiro Quartil (Q1):", q1)
print("Primeiro Quartil (Q2):", q2)
print("Primeiro Quartil (Q3):", q3)

###
df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')

print(df_transacoes)

q1_preco = df_transacoes['preco'].quantile(0.25)
q2_preco = df_transacoes['preco'].quantile(0.50)
q3_preco = df_transacoes['preco'].quantile(0.75)

print("Preço Q1:", q1_preco)
print("Preço Mediana Q2:", q2_preco)
print("Preço Q3:", q3_preco)

# variável para o gráfico
contagem_operacao = df_transacoes['operacao'].value_counts()

# criando grafico de barras
contagem_operacao.plot(kind='bar',title='Tipos de Operação')

# mostrando gráfico
plt.show()