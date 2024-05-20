import pandas as pd

# Defina os intervalos de datas
intervalos_de_datas = {
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

# Leia o CSV
df = pd.read_csv('games.csv')

# Converta a coluna de data para datetime
df['GAME_DATE_EST'] = pd.to_datetime(df['GAME_DATE_EST'])

# Função para filtrar e salvar os dados para cada intervalo
def filtrar_e_salvar_dados(intervalos, df):
    for periodo, (inicio, fim) in intervalos.items():
        # Filtrar os dados dentro do intervalo
        mask = (df['GAME_DATE_EST'] >= inicio) & (df['GAME_DATE_EST'] <= fim)
        df_filtrado = df.loc[mask]
        
        # Substituir barras por sublinhados no nome do período
        nome_arquivo = periodo.replace('/', '_')
        
        # Salvar em um novo arquivo CSV
        df_filtrado.to_csv(f'{nome_arquivo}.csv', index=False)

# Chame a função
filtrar_e_salvar_dados(intervalos_de_datas, df)

print("Tabelas separadas foram salvas com sucesso.")
