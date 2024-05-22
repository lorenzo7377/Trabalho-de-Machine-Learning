import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

accuracy_scores = []

# Configurando a janela para os gráficos
plt.figure(figsize=(15, 10))

# Iteração sobre os anos
for idx, year in enumerate(range(2003, 2022)):
    # Leitura dos dados
    print(f'-------------------------------{year}/{year+1}----------------------------------')
    df = pd.read_csv(f'./TPnormal/{year}_{year+1}.csv')
    df2 = pd.read_csv(f'./Playoff/{year}_{year+1}.csv')

    # Definição das features e da variável alvo
    features = [
        'FG_PCT_home', 'FT_PCT_home', 'FG3_PCT_home', 'AST_home', 'REB_home',
        'FG_PCT_away', 'FT_PCT_away', 'FG3_PCT_away', 'AST_away', 'REB_away'
    ]
    target = 'HOME_TEAM_WINS'

    # Preparação dos dados de treinamento e teste
    X_train = df[features].fillna(0)
    y_train = df[target]
    X_test = df2[features].fillna(0)
    y_test = df2[target]

    # Criação e treinamento do modelo de regressão logística
    logistic_model = LogisticRegression(max_iter=1000)
    logistic_model.fit(X_train, y_train)

    # Realização de previsões
    y_pred = logistic_model.predict(X_test)

    # Avaliação do modelo
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_scores.append(accuracy)

    print(f'Porcentagem de acertos para o ano {year}_{year+1}:', accuracy)

    predictions = logistic_model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, predictions))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    cv_scores = cross_val_score(logistic_model, X_train, y_train, cv=5)
    print('Acurácia (Validação Cruzada):', cv_scores)
    print('Acurácia Média (Validação Cruzada):', cv_scores.mean())

    # Plotagem do gráfico
    plt.subplot(4, 5, idx+1)
    plt.scatter(X_test['FT_PCT_away'], y_test, c=y_pred, cmap='coolwarm', marker='o', edgecolor='k', s=100)
    plt.title(f'FT_PCT_away vs. {target}')
    plt.xlabel('FT_PCT_away')
    plt.ylabel(target)
    plt.colorbar(label='Classificação Prevista')

# Ajustando a aparência da janela
plt.tight_layout()
plt.show()
