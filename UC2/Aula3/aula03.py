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
