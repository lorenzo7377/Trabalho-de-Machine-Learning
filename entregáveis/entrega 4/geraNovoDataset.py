import pandas as pd

# Carrega o arquivo CSV
data = pd.read_csv('./dataset/games.csv')

# Cria um DataFrame vazio para armazenar o número de vitórias de cada equipe em cada ano
years = list(range(2003, 2023))
teams_wins_by_year = pd.DataFrame(columns=['TEAM_ID'] + [f'{year}_HOME_WINS' for year in years] + [f'{year}_AWAY_WINS' for year in years] + [f'{year}_TOTAL_WINS' for year in years])

# Função para extrair o ano de uma data no formato "yyyy-mm-dd"
def extract_year(date):
    return int(date.split('-')[0])

# Calcula o número de vitórias em casa e fora de casa para cada equipe em cada ano
for team_id in data['HOME_TEAM_ID'].unique():
    team_data = data[(data['HOME_TEAM_ID'] == team_id) | (data['VISITOR_TEAM_ID'] == team_id)]
    team_wins_by_year = {'TEAM_ID': team_id}
    for year in years:
        home_wins = len(team_data[(team_data['HOME_TEAM_ID'] == team_id) & (team_data['GAME_DATE_EST'].str.split('-').str[0].astype(int) == year) & (team_data['HOME_TEAM_WINS'] == 1)])
        away_wins = len(team_data[(team_data['VISITOR_TEAM_ID'] == team_id) & (team_data['GAME_DATE_EST'].str.split('-').str[0].astype(int) == year) & (team_data['HOME_TEAM_WINS'] == 0)])
        team_wins_by_year[f'{year}_HOME_WINS'] = home_wins
        team_wins_by_year[f'{year}_AWAY_WINS'] = away_wins
    # Calcula o total de vitórias para cada ano
    for year in years:
        total_home_wins = team_wins_by_year[f'{year}_HOME_WINS']
        total_away_wins = team_wins_by_year[f'{year}_AWAY_WINS']
        team_wins_by_year[f'{year}_TOTAL_WINS'] = total_home_wins + total_away_wins
    # Concatena o DataFrame temporário com o DataFrame principal
    teams_wins_by_year = pd.concat([teams_wins_by_year, pd.DataFrame(team_wins_by_year, index=[0])], ignore_index=True)

# Salva o resultado em um novo arquivo CSV
teams_wins_by_year.to_csv('teams_wins_by_year.csv', index=False)
