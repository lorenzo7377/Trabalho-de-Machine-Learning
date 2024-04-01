import numpy as np
import matplotlib.pyplot as plt
import csv

# Listas para armazenar os valores das colunas
coluna1 = []
coluna2 = []

# Abra o arquivo CSV
with open('db.csv', 'r') as arquivo:
    # Crie um leitor CSV
    leitor_csv = csv.reader(arquivo)
    
    # Itere sobre as linhas do arquivo
    for linha in leitor_csv:
        # Acesse as colunas desejadas
        valor_da_coluna1 = float(linha[0])  # Converta para float
        valor_da_coluna2 = float(linha[1])  # Converta para float
        
        # Adicione os valores às listas
        coluna1.append(valor_da_coluna1)
        coluna2.append(valor_da_coluna2)

# Converta as listas para arrays numpy
temperatura = np.array(coluna1).reshape(-1, 1)
bicicletas = np.array(coluna2)

# Cálculo dos Coeficientes com Mínimos Quadrados
X_b = np.c_[np.ones((len(temperatura), 1)), temperatura]
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(bicicletas)

# Visualização dos Dados e do Ajuste Linear
plt.scatter(temperatura, bicicletas, color='blue', label='Dados simulados')
line_x = np.linspace(0, 40, 100).reshape(100, 1)
line_y = theta_best[0] + theta_best[1] * line_x
plt.plot(line_x, line_y, color='red', label='Ajuste Linear')
plt.xlabel('Temperatura')
plt.ylabel('Bicicletas')
plt.title('Relação entre Temperatura e Número de Bicicletas Vendidas')
plt.legend()
plt.show()

# Predição de bicicletas com o Modelo
X_new = np.array([[31], [3]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
bicicletas_previstas = X_new_b.dot(theta_best)
print(bicicletas_previstas)
