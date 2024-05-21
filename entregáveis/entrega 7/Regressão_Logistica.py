import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv('./databasejogos.csv')
df2 = pd.read_csv('./databasejogosPO.csv')

features = [
    'FG_PCT_home', 'FT_PCT_home', 'FG3_PCT_home', 'AST_home', 'REB_home',
    'FG_PCT_away', 'FT_PCT_away', 'FG3_PCT_away', 'AST_away', 'REB_away'
]
target = 'HOME_TEAM_WINS'

X_train = df[features].fillna(0)  # Tratamento de possíveis valores faltantes
y_train = df[target]

X_test = df2[features].fillna(0)  # Tratamento de possíveis valores faltantes
y_test = df2[target]

logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train, y_train)
y_pred = logistic_model.predict(X_test)

print('Porcentagem de acertos:', metrics.accuracy_score(y_test, y_pred))

predictions = logistic_model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

cv_scores = cross_val_score(logistic_model, X_train, y_train, cv=5)
print('Acurácia (Validação Cruzada):', cv_scores)
print('Acurácia Média (Validação Cruzada):', cv_scores.mean())
