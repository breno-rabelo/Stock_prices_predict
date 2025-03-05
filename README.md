# Previsão de Ações e Estratégia de Trading

Este projeto utiliza dados financeiros para prever os preços futuros de ações e simula uma estratégia de trading automatizada baseada nas previsões. O modelo é construído usando regressão linear e incorpora médias móveis como features.

## Tecnologias Utilizadas
- Python
- Yahoo Finance API (yfinance)
- Pandas
- Scikit-learn
- Matplotlib

## Como Usar

1. Instale as dependências necessárias:
   ```bash
   pip install yfinance pandas scikit-learn matplotlib
   ```
2. Execute o script Python:
   ```bash
   python script.py
   ```
3. Digite o ticker da ação quando solicitado.
4. O script irá baixar os dados históricos, treinar um modelo de previsão e executar uma simulação de trading.
5. Os resultados serão exibidos no terminal e em um gráfico de previsão.

## Estratégia de Trading
- Compra quando o preço previsto é maior que o preço atual.
- Venda quando o preço previsto é menor que o preço atual.
- O saldo inicial é de $300.000, e todas as compras usam o saldo disponível.

## Aviso
Este projeto é apenas para fins educacionais e não deve ser usado para tomar decisões reais de investimento.

