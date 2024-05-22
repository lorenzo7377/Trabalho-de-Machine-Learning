import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Carregar os dados
data_path = './TPnormal/2003_2004.csv'
data_path2 = './Playoff/2003_2004.csv'
data = pd.read_csv(data_path)
data2 = pd.read_csv(data_path2)

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

for column in data2.columns:
    if data2[column].dtype == 'object':
        try:
            data2[column] = pd.to_datetime(data2[column])
            data2[column + '_year'] = data2[column].dt.year
            data2[column + '_month'] = data2[column].dt.month
            data2[column + '_day'] = data2[column].dt.day
        except ValueError:
            pass  # Mantém a coluna original se não puder ser convertida em data
data2 = data2.select_dtypes(include=[np.number])  # Seleciona apenas colunas numéricas

# Selecionar automaticamente todas as features, excluindo a coluna alvo
target = 'HOME_TEAM_WINS'  # Coluna alvo
excluded_features = ['PTS_away', 'PTS_home', target]
features = data.columns.drop(excluded_features)  # Remove as colunas especificadas da lista de features
x_train = data[features].fillna(0)  # Tratamento de valores faltantes
y_train = data[target]

x_test = data2[features].fillna(0)  # Tratamento de valores faltantes
y_test = data2[target]

# Criar e treinar o modelo Random Forest
random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)
random_forest_model.fit(x_train, y_train)

# Fazer previsões e avaliar o modelo
predictions = random_forest_model.predict(x_test)
print("Classification Report:")
print(classification_report(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Mostrar as importâncias das features
feature_importances = pd.DataFrame(random_forest_model.feature_importances_,
                                   index=x_train.columns,
                                   columns=['importance']).sort_values('importance', ascending=False)
print("Feature Importances:")
print(feature_importances)

# Validar o modelo usando validação cruzada
cv_scores = cross_val_score(random_forest_model, x_train, y_train, cv=5, scoring='accuracy')
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())
