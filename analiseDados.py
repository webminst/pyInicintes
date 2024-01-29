import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados de um arquivo CSV
dados = pd.read_csv("dados.csv")

# Realizar análise exploratória dos dados
# Exemplo: exibir estatísticas descritivas
estatisticas = dados.describe()
print(estatisticas)

# Criar gráfico de barras
plt.bar(dados["categoria"], dados["quantidade"])
plt.xlabel("Categoria")
plt.ylabel("Quantidade")
plt.title("Distribuição de Categorias")
plt.show()