import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
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

print('Porcentagem de acertos:', metrics.accuracy_score(y_test, y_pred))

predictions = logistic_model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

time_desejado =  1610612754
time_visitante = 1610612751

# Filtragem dos dados para o time desejado (time da casa)
df_time = df[df['HOME_TEAM_ID'] == time_desejado].copy()

# Filtragem dos dados para o time desejado (time visitante)
df_time_visitante = df[df['VISITOR_TEAM_ID'] == time_visitante].copy()

# Tratamento de valores ausentes para o time da casa
df_time['PTS_home'].fillna(0, inplace=True)
df_time['FG_PCT_home'].fillna(0, inplace=True)
df_time['FT_PCT_home'].fillna(0, inplace=True)
df_time['FG3_PCT_home'].fillna(0, inplace=True)
df_time['AST_home'].fillna(0, inplace=True)
df_time['REB_home'].fillna(0, inplace=True)

# Tratamento de valores ausentes para o time visitante
df_time_visitante['PTS_away'].fillna(0, inplace=True)
df_time_visitante['FG_PCT_away'].fillna(0, inplace=True)
df_time_visitante['FT_PCT_away'].fillna(0, inplace=True)
df_time_visitante['FG3_PCT_away'].fillna(0, inplace=True)
df_time_visitante['AST_away'].fillna(0, inplace=True)
df_time_visitante['REB_away'].fillna(0, inplace=True)

# Cálculo das médias para o time da casa
media_pontos_casa = df_time['PTS_home'].mean()
media_fgpct_casa = df_time['FG_PCT_home'].mean()
media_ftpct_casa = df_time['FT_PCT_home'].mean()
media_fg3_casa = df_time['FG3_PCT_home'].mean()
media_ast_casa = df_time['AST_home'].mean()
media_reb_casa = df_time['REB_home'].mean()

# Cálculo das médias para o time visitante
media_pontos_visitante = df_time_visitante['PTS_away'].mean()
media_fgpct_visitante = df_time_visitante['FG_PCT_away'].mean()
media_ftpct_visitante = df_time_visitante['FT_PCT_away'].mean()
media_fg3_visitante = df_time_visitante['FG3_PCT_away'].mean()
media_ast_visitante = df_time_visitante['AST_away'].mean()
media_reb_visitante = df_time_visitante['REB_away'].mean()

# Imprimir as médias
print("Média de pontos do time da casa:", media_pontos_casa)
print("Média FG_PCT_home do time da casa:", media_fgpct_casa)
print("Média FT_PCT_home do time da casa:", media_ftpct_casa)
print("Média FG3_PCT_home do time da casa:", media_fg3_casa)
print("Média AST_home do time da casa:", media_ast_casa)
print("Média REB_home do time da casa:", media_reb_casa)

print("Média pontos do time visitante:", media_pontos_visitante)
print("Média FG_PCT_away do time visitante:", media_fgpct_visitante)
print("Média FT_PCT_away do time visitante:", media_ftpct_visitante)
print("Média FG3_PCT_away do time visitante:", media_fg3_visitante)
print("Média AST_away do time visitante:", media_ast_visitante)
print("Média REB_away do time visitante:", media_reb_visitante)

teste_vencedor = { 
    'FG_PCT_home':media_fgpct_casa,'FT_PCT_home': media_ftpct_casa, 'FG3_PCT_home': media_fg3_casa, 'AST_home': media_ast_casa, 'REB_home': media_reb_casa,
    'FG_PCT_away':media_fgpct_visitante,'FT_PCT_away': media_ftpct_visitante, 'FG3_PCT_away': media_fg3_visitante, 'AST_away': media_ast_visitante, 'REB_away': media_reb_visitante
}

dft = pd.DataFrame(data=teste_vencedor, index=[0])

print(dft)

resultado = logistic_model.predict(dft)

if (resultado == 0):
    print("\n||||||||||||||||||||||\nTime da visitante venceu\n||||||||||||||||||||||\n")
else:
    print("\n||||||||||||||||||||||\nTime da casa venceu\n||||||||||||||||||||||\n")

cv_scores = cross_val_score(logistic_model, X_train, y_train, cv=5)
print('Acurácia (Validação Cruzada):', cv_scores)
print('Acurácia Média (Validação Cruzada):', cv_scores.mean())