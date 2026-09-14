import pandas as pd
import numpy as np

filmes = {
    'titulo': ["Lago Azul","Agente Secreto","Gênio Indomável"],
    'categoria': ["Romance","Ação","Drama"],
    'ano': ["1980","2025","1997"]
}

tabela_filmes = pd.DataFrame(filmes)
print(filmes)
print(type(filmes))
print(tabela_filmes)
print(type(tabela_filmes))


quantidade = int(input("Quantos filmes dseja adicionar? "))
contador = 0

while contador < quantidade:
    titulo = input("Digite o título do filme: ")
    categoria = input("Digite sua categoria: ")
    ano = input("Digite o ano de lançamento: ")

    filmes["titulo"] = titulo
    filmes["categoria"] = categoria
    filmes["ano"] = ano

    contador += 1

print(filmes)