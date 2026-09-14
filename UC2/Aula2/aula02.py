import pandas as pd
import numpy as np
import openpyxl

# numeros_impares = [43, 55, 1, 3, 11, 27, 109]
# numeros_seq = [2, 3, 4, 5, 6, 7]

# # print(type(numeros_impares))

# serie_impares = pd.Series(numeros_impares)

# print(serie_impares)
# # print(type(serie_impares))

# # print(numeros_impares[3])
# # print(numeros_impares[4])
# # print(numeros_impares[0])

# # print(serie_impares.sum())
# # print(serie_impares.median())
# # print(serie_impares.min())
# # print(serie_impares.max())
# # print(len(serie_impares))
# # print(serie_impares.describe())
# # print(serie_impares[serie_impares>50])

# # serie2_impares = pd.Series(
# #     numeros_impares, 
# #     index =['a','b','c','d','e','f','g']
# #     )

# # print(serie2_impares)

# filmes = {
#     'titulo': ["Lago Azul","Agente Secreto","Gênio Indomável"],
#     'categoria': ["Romance","Ação","Drama"],
#     'ano': ["1980","2025","1997"]
# }

# tabela_filmes = pd.DataFrame(filmes)
# print(filmes)
# print(type(filmes))
# print(tabela_filmes)
# print(type(tabela_filmes))


# quadrado_serie_impares = serie_impares*serie_impares
# print(quadrado_serie_impares)

### LEITURA ARQUIVOS XLSX
# variável      # comando      # caminho arquivo  # argumentos leitura
leitura_invest = pd.read_excel("base_invest.xlsx",sheet_name=1)

print(leitura_invest)