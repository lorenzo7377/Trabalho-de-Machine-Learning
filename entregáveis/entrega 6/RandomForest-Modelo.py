import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Carregar os dados
data_path = './databasejogos.csv'
data = pd.read_csv(data_path)

# Tratar colunas de data e remover colunas não numéricas
for column in data.columns:
    if data[column].dtype == 'object':
        try:
            data[column] = pd.to_datetime(data[column])
            data[column + '_year'] = data[column].dt.year
            data[column + '_month'] = data[column].dt.month
            data[column + '_day'] = data[column].dt.day
        except ValueError:
            pass  # Mantém a coluna original se não puder ser convertida em data
data = data.select_dtypes(include=[np.number])  # Seleciona apenas colunas numéricas

# Selecionar automaticamente todas as features, excluindo a coluna alvo
target = 'HOME_TEAM_WINS'  # Coluna alvo
excluded_features = ['PTS_away', 'PTS_home', target]
features = data.columns.drop(excluded_features)  # Remove as colunas especificadas da lista de features
X = data[features].fillna(0)  # Tratamento de valores faltantes
y = data[target]

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo Random Forest
random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)
random_forest_model.fit(X_train, y_train)

# Fazer previsões e avaliar o modelo
predictions = random_forest_model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Mostrar as importâncias das features
feature_importances = pd.DataFrame(random_forest_model.feature_importances_,
                                   index = X_train.columns,
                                   columns=['importance']).sort_values('importance', ascending=False)
print("Feature Importances:")
print(feature_importances)

# Validar o modelo usando validação cruzada
cv_scores = cross_val_score(random_forest_model, X, y, cv=5, scoring='accuracy')
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())
