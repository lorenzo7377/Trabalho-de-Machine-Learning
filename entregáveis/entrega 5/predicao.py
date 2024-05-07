import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv('./databasejogos.csv')

features = [
    'FG_PCT_home', 'FT_PCT_home', 'FG3_PCT_home', 'AST_home', 'REB_home',
    'FG_PCT_away', 'FT_PCT_away', 'FG3_PCT_away', 'AST_away', 'REB_away'
]
target = 'HOME_TEAM_WINS'

X = df[features].fillna(0)  # Tratamento de possíveis valores faltantes
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
y_pred = logistic_model.predict(X_test)

print('porcentagem ', metrics.accuracy_score(y_test, y_pred))

predictions = logistic_model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

teste_vencedor = { 
    'FG_PCT_home': 0.5, 'FT_PCT_home':0.54, 'FG3_PCT_home':0.39, 'AST_home':27, 'REB_home':48,
    'FG_PCT_away':0.6, 'FT_PCT_away':0.7, 'FG3_PCT_away':0.6, 'AST_away':34, 'REB_away':57
}

dft = pd.DataFrame(data = teste_vencedor, index=[0])

print(dft)

resultado = logistic_model.predict(dft)

if (resultado == 0):
    print("Time da visitante venceu")
else:
    print("Time da casa venceu")