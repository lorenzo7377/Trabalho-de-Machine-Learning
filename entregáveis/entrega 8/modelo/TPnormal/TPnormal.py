import pandas as pd

# Defina os intervalos de datas
intervalos_de_datas = {
    '2003/2004': ['2003-10-28', '2004-04-14'],
    '2004/2005': ['2004-11-02', '2005-04-23'],
    '2005/2006': ['2005-11-01', '2006-04-21'],
    '2006/2007': ['2006-10-31', '2007-04-18'],
    '2007/2008': ['2007-10-30', '2008-04-16'],
    '2008/2009': ['2008-10-28', '2009-04-17'],
    '2009/2010': ['2009-10-27', '2010-04-14'],
    '2010/2011': ['2010-10-26', '2011-04-13'],
    '2011/2012': ['2011-12-25', '2012-04-28'],
    '2012/2013': ['2012-10-30', '2013-04-20'],
    '2013/2014': ['2013-10-29', '2014-04-16'],
    '2014/2015': ['2014-10-04', '2015-04-15'],
    '2015/2016': ['2015-10-27', '2016-04-13'],
    '2016/2017': ['2016-10-25', '2017-04-12'],
    '2017/2018': ['2017-10-17', '2018-04-11'],
    '2018/2019': ['2018-10-16', '2019-04-10'],
    '2019/2020': ['2019-10-22', '2020-03-11'],
    '2020/2021': ['2020-12-22', '2021-05-16'],
    '2021/2022': ['2021-10-19', '2022-04-10'],
}

# Leia o CSV
df = pd.read_csv('./games.csv')

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
