# Esses dados foram fornecidos pelos professores Eliel Marlon de Lima Pinto Moreira e Tarcísio Lopes de Almeida Sousa

# Cálculo do Valor de Z
# O valor Z é uma medida de quantos desvios padrão um elemento X está longe da média.
# Fórmula: Z = ( X − μ ) / σ , onde:
# X é o valor de interesse
# μ é a média
# σ é o desvio padrão

import numpy as np

# Função para calcular o valor de Z
def calcular_z(x, media, desvio_padrao):
    z = (x - media) / desvio_padrao
    return z

# Exemplo de uso
x = 92
media = 80
desvio_padrao = 5
z = calcular_z(x, media, desvio_padrao)
print(f"Valor de Z: {z}")

# Cálculo da Probabilidade Acumulada até Z
# A função norm.cdf da biblioteca scipy.stats calcula a probabilidade acumulada até um dado valor de Z.
from scipy.stats import norm

# Função para calcular a probabilidade acumulada até Z
def probabilidade_acumulada_z(z):
    prob = norm.cdf(z)
    return prob

# Exemplo de uso
z = 2.4
prob = probabilidade_acumulada_z(z)
print(f"Probabilidade acumulada até Z: {prob}")

# Cálculo do Valor de Z para uma dada Probabilidade
# A função norm.ppf da biblioteca scipy.stats calcula o valor de Z para uma dada probabilidade.
from scipy.stats import norm

# Função para calcular o valor de Z para uma dada probabilidade
def calcular_z_probabilidade(probabilidade):
    z = norm.ppf(probabilidade)
    return z

# Exemplo de uso
probabilidade = 0.9918024640754038
z = calcular_z_probabilidade(probabilidade)
print(f"Valor de Z para a probabilidade {probabilidade}: {z}")

# Cálculo da Probabilidade Acumulada até um Valor X
# A função norm.cdf pode ser usada para calcular a probabilidade acumulada até um valor X, dados a média e o desvio padrão.