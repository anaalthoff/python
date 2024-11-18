# Bibliotecas Utilizadas
# Pandas: Para manipulação e análise de dados.
# NumPy: Para operações matemáticas e estatísticas.
# Scipy: Para cálculos estatísticos avançados.
# Scikit-learn: Para modelagem e análise preditiva.

# Resumo dos Comandos Utilizados
# Operação	Biblioteca	Comando
# Média	pandas	df['coluna'].mean()
# Desvio Padrão	pandas	df['coluna'].std()
# Soma	pandas	df['coluna'].sum()
# Mediana	pandas	df['coluna'].median()
# Contagem	pandas	df['coluna'].count()
# Variância	pandas	df['coluna'].var()
# Inclinação (Slope)	scipy.stats	stats.linregress(X, Y).slope
# Interceptação (Intercept)	scipy.stats	stats.linregress(X, Y).intercept
# R²	scipy.stats	(stats.linregress(X, Y).rvalue)**2
# Regressão Linear	scikit-learn	modelo.fit(X, Y) seguido de modelo.coef_ e modelo.intercept_
# Plotagem de Gráfico	matplotlib	plt.scatter(), plt.plot(), plt.show()

# Esses dados foram fornecidos pelos professores Eliel Marlon de Lima Pinto Moreira e Tarcísio Lopes de Almeida Sousa

# Importar bibliotecas e carregar dados
import pandas as pd
import numpy as np

# Exemplo de DataFrame
dados = {
    'Valores': [10, 20, 20, 40, 50, 50, 50, 60, 70, 80]
}
df = pd.DataFrame(dados)
print(df)

# Cálculo da Média
# A média é a soma de todos os valores dividida pelo número de observações.
media = df['Valores'].mean()
print(f"Média: {media}")

# Cálculo do Desvio Padrão
# O desvio padrão mede a dispersão dos dados em relação à média.
desvio_padrao = df['Valores'].std()
print(f"Desvio Padrão: {desvio_padrao}")

# Cálculo da Soma
# A soma total dos valores.
soma = df['Valores'].sum()
print(f"Soma: {soma}")

# Cálculo da Mediana
# A mediana é o valor central que divide o conjunto de dados em duas partes iguais.
mediana = df['Valores'].median()
print(f"Mediana: {mediana}")

# Cálculo da Contagem
# A contagem total de observações.
contagem = df['Valores'].count()
print(f"Contagem: {contagem}")

# Cálculo da Variância
# A variância mede a variabilidade dos dados em relação à média.
variancia = df['Valores'].var()
print(f"Variância: {variancia}")

# Regressão Linear
# A regressão linear é uma técnica estatística para modelar a relação entre uma variável dependente e uma ou mais variáveis independentes. Abaixo será exemplificado a regressão linear simples (uma variável independente).

# Conjunto de dados de exemplo
dados_reg = {

    'X': [1, 2, 3, 4, 5],

    'Y': [2, 4, 5, 4, 5]
}
df_reg = pd.DataFrame(dados_reg)
print(df_reg)

# Cálculo da Inclinação (Slope) e Interceptação (Intercept)
from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(df_reg['X'], df_reg['Y'])

print(f"Inclinação (Slope): {slope}")
print(f"Interceptação (Intercept): {intercept}")

# Cálculo do Coeficiente de Determinação (R²)
# O R² indica a proporção da variabilidade da variável dependente que é explicada pelo modelo.
r_squared = r_value**2
print(f"R²: {r_squared}")

# Plotando o Gráfico de Regressão Linear
# Usar a biblioteca matplotlib para plotar o gráfico de regressão linear.
import matplotlib.pyplot as plt

# Dados de entrada
X = df_reg['X']
Y = df_reg['Y']

# Calculando os valores previstos pela regressão linear
Y_pred = intercept + slope * X

# Plotando os dados e a linha de regressão
plt.scatter(X, Y, color='blue', label='Dados')
plt.plot(X, Y_pred, color='red', label='Regressão Linear')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regressão Linear Simples')
plt.legend()
plt.show()