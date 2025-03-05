# https://medium.com/@deepml1818/predicting-stock-prices-with-machine-learning-in-python-a-step-by-step-guide-c53f36ab1ccd
import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Pegando informacao historica da acao
ticker = input('Digite o ticket da acao: ')
data = yf.download(ticker)

# Mostrar as ultimas linhas da consulta
print(data.tail())

# Calculando as medias moveis dos precos de fechamento
data['MM_10'] = data['Close'].rolling(window=10).mean()
data['MM_50'] = data['Close'].rolling(window=50).mean()

# Apagar valores nulos
data = data.dropna()

# Definir os recusos e alvos
X = data[['Close', 'MM_10', 'MM_50']] # Define os recursos incluindo preco de fechamento e medias moveis
Y = data['Close'].shift(-1).dropna() # Define o alvo deslocando um dia, para prever o proximo dia
X = X[:-1]

# Separando informacoes para teste e treino com 20% dos dados reservados para teste
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

# Treinar o modelo preditivo
model = LinearRegression()
model.fit(X_train, Y_train)

# Fazer as previsoes
predicoes = model.predict(X_test)

# Avaliar confiabilidade do modelo
mse = mean_squared_error(Y_test, predicoes)
r2 = r2_score(Y_test, predicoes)

print(f'Mean Squared Error: {mse}')
print(f'R² Score: {r2}')

# Visualizar os resultados da predicao
plt.figure(figsize= (15,6))
plt.plot(Y_test.index, Y_test.values, label='Preco Atual')
plt.plot(Y_test.index, Y_test.values, label='Previsao')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Atual X Preco Previsto')
plt.legend()

# Implementar um sistema basico de trading baseado nas previsoes
# A estrategia de Trade consiste em Comprar quando o preco previsto e maior que o preco Atual e Vender quando o preco previsto for menor que o preco atual

# Valor hipotetico disponivel para invetimento
valor_inicial = 300000
balanco = valor_inicial
posicao = 0

for i in range(len(X_test)):
    valor_atual = float(X_test.iloc[i]['Close'])
    previsao_valor = float(predicoes[i])

    if previsao_valor > valor_atual and balanco >= valor_atual:
        aviso_compra = int(balanco // valor_atual)
        # Garantir a compra de pelo menos uma acao
        if aviso_compra > 0:
            posicao += aviso_compra
            balanco -= aviso_compra * valor_atual
            print(f'Compra de {aviso_compra} pelo preco: {valor_atual:.2f}')

        elif previsao_valor < valor_atual and posicao > 0:
            balanco += posicao * valor_atual
            print(f'Venda {posicao} pelo preco: {valor_atual:.2f}')
            posicao = 0

# Calcular o patrimonio com os valores das transacoes
valor_final = balanco + (posicao * float(X_test.iloc[-1]['Close']))
lucro = valor_final - valor_inicial
print(f"Valor Final: ${valor_final:.2f}")
print(f"Lucro: $ {lucro:.2f}")