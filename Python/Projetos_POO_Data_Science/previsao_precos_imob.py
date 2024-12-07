import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Suponha que você tenha um conjunto de dados de imóveis com informações relevantes, como tamanho, localização, número de quartos, etc.
# Vamos criar um DataFrame de exemplo para demonstração.

data = {
    'Tamanho (metros quadrados)': [80, 100, 120, 150, 200],
    'Número de Quartos': [2, 3, 3, 4, 4],
    'Localização': ['Centro', 'Subúrbio', 'Centro', 'Subúrbio', 'Subúrbio'],
    'Preço (em milhares de reais)': [150, 200, 250, 300, 350]
}

df = pd.DataFrame(data)

# Codificar a variável 'Localização' em variáveis dummy
df = pd.get_dummies(df, columns=['Localização'], drop_first=True)

# Separar as features (X) e o alvo (y)
X = df.drop('Preço (em milhares de reais)', axis=1)
y = df['Preço (em milhares de reais)']

# Dividir os dados em conjunto de treinamento e conjunto de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar um modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o desempenho do modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Erro Quadrático Médio (MSE): {mse}")
print(f"Coeficiente de Determinação (R²): {r2}")

# Visualizar as previsões vs. valores reais
plt.scatter(y_test, y_pred)
plt.xlabel("Preço Real")
plt.ylabel("Preço Previsto")
plt.title("Preço Real vs. Preço Previsto")
plt.show()