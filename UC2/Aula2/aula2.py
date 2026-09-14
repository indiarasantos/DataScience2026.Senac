import pandas as pd
import numpy as np

#LOC
#ILOC
#QUERY


filmes = {
    'título': ["Lago Azul","Agente Secreto","Gênio Indomável","A Freira","Brinquedo Assassino","Top Gun"],
    'categoria': ["Romance","Ação","Drama","Terror","Comédia","Aventura"],
    'ano': ["1980","2025","1997","2022","1995","1986"],
    'faturamento': [6.5,4,5.5,3,9,7.2]
}

indices = ['A','B','C','D','E','F']

tabela_filmes = pd.DataFrame(filmes, index=indices)
print(filmes)
print(type(filmes))
print(tabela_filmes)
print(type(tabela_filmes))

print("--ILOC--")
print(tabela_filmes.iloc[0])
print(tabela_filmes.iloc[1])
print(tabela_filmes.iloc[-1])
print(tabela_filmes.iloc[2,2])
print(tabela_filmes.iloc[1:4])

print("--LOC--")
print(tabela_filmes.loc['B'])
print(tabela_filmes.loc['A'])
print(tabela_filmes.loc['C'])
print(tabela_filmes.loc['B':'E'])

print("--QUERY--")
consulta1 = tabela_filmes.query("faturamento == 5.5")
print(consulta1)
