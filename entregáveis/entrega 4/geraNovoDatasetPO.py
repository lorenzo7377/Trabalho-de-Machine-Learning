import pandas as pd

# Carrega o arquivo CSV
data = pd.read_csv('./dataset/games.csv')

# Define os períodos de tempo dos playoffs de cada temporada
playoff_periods = {
    '2003/2004': ['2004-04-17', '2004-06-15'],
    '2004/2005': ['2005-04-24', '2005-06-23'],
    '2005/2006': ['2006-04-22', '2006-06-20'],
    '2006/2007': ['2007-04-21', '2007-06-21'],
    '2007/2008': ['2008-04-19', '2008-06-17'],
    '2008/2009': ['2009-04-18', '2009-06-14'],
    '2009/2010': ['2010-04-17', '2010-06-17'],
    '2010/2011': ['2011-04-16', '2011-06-12'],
    '2011/2012': ['2012-04-28', '2012-06-21'],
    '2012/2013': ['2013-04-20', '2013-06-20'],
    '2013/2014': ['2014-04-19', '2014-06-15'],
    '2014/2015': ['2015-04-18', '2015-06-16'],
    '2015/2016': ['2016-04-16', '2016-06-19'],
    '2016/2017': ['2017-04-15', '2017-06-12'],
    '2017/2018': ['2018-04-14', '2018-06-08'],
    '2018/2019': ['2019-04-13', '2019-06-13'],
    '2019/2020': ['2020-08-17', '2020-10-11'],
    '2020/2021': ['2021-05-22', '2021-07-20'],
    '2021/2022': ['2022-04-16', '2022-06-16']
}

# Cria um DataFrame vazio para armazenar as estatísticas de cada equipe em cada período de playoffs
teams_stats_by_playoffs = pd.DataFrame(columns=['TEAM_ID'] + [f'{period}_HOME_GAMES' for period in playoff_periods.keys()] + [f'{period}_AWAY_GAMES' for period in playoff_periods.keys()] + [f'{period}_HOME_WINS' for period in playoff_periods.keys()] + [f'{period}_AWAY_WINS' for period in playoff_periods.keys()] + [f'{period}_TOTAL_GAMES' for period in playoff_periods.keys()])

# Função para extrair o ano de uma data no formato "yyyy-mm-dd"
def extract_year(date):
    return int(date.split('-')[0])

# Calcula o número de jogos em casa e fora de casa, bem como o número de vitórias em casa e fora de casa para cada equipe em cada período de playoffs
for team_id in data['HOME_TEAM_ID'].unique():
    team_data = data[(data['HOME_TEAM_ID'] == team_id) | (data['VISITOR_TEAM_ID'] == team_id)]
    team_stats_by_playoffs = {'TEAM_ID': team_id}
    for period, dates in playoff_periods.items():
        start_date, end_date = dates
        playoff_data = team_data[(team_data['GAME_DATE_EST'].between(start_date, end_date))]
        home_games = len(playoff_data[playoff_data['HOME_TEAM_ID'] == team_id])
        away_games = len(playoff_data[playoff_data['VISITOR_TEAM_ID'] == team_id])
        total_games = home_games + away_games
        home_wins = len(playoff_data[(playoff_data['HOME_TEAM_ID'] == team_id) & (playoff_data['HOME_TEAM_WINS'] == 1)])
        away_wins = len(playoff_data[(playoff_data['VISITOR_TEAM_ID'] == team_id) & (playoff_data['HOME_TEAM_WINS'] == 0)])
        team_stats_by_playoffs[f'{period}_HOME_GAMES'] = home_games
        team_stats_by_playoffs[f'{period}_AWAY_GAMES'] = away_games
        team_stats_by_playoffs[f'{period}_HOME_WINS'] = home_wins
        team_stats_by_playoffs[f'{period}_AWAY_WINS'] = away_wins
        team_stats_by_playoffs[f'{period}_TOTAL_GAMES'] = total_games
    # Concatena o DataFrame temporário com o DataFrame principal
    teams_stats_by_playoffs = pd.concat([teams_stats_by_playoffs, pd.DataFrame(team_stats_by_playoffs, index=[0])], ignore_index=True)

# Salva o resultado em um novo arquivo CSV
teams_stats_by_playoffs.to_csv('novodataset.csv', index=False)
