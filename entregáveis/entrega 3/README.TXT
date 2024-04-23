MINI TRABALHO 3: Exploração dos dados
equipe: 1

Membros:
Artur Jackson Leal Fontinele - 211030943
Fause Carlos Mascarenhas Lustosa Junior - 211031691
Lorenzo de Lima Alves dos Santos - 190032821
Pedro Cabeceira de Freitas - 211043727
Rafael Kenji Taira - 190044128
Thiago França Vale Oliveira - 170119429

- Nossos dados foram coletados na plataforma kaggle (https://www.kaggle.com/datasets/nathanlauga/nba-games).

## Engenharia de atributo

Nós utilizamos a engenharia de atributos (feature engineering) para separar os dados da nossa base de dados e deixar ela o mais limpa e apenas com os dados que serão necessários para a nossa análise. Conseguimos excluir uma coluna de status dos jogos, pois todos já acabaram e a coluna de id da liga, pois todos os jogos são da NBA, logo ela não agrega em nada.

## Normalização

Não achamos necessário utilizar a normalização, pois nossos dados não tem uma distância muito grande, eles variam de 0 até 150, independente da sua estatística, por exemplo, só vamos chegar perto de 100 quando é a pontuação de um jogo, mas a pontuação individuais não passam de 70 e os rebotes e assistências não passam de 20.

## Análise detalhada de Atributos

Para evitar cometer erros ao utilizar dados de forma equivocada no projeto de aprendizagem de máquina, realizamos uma reunião onde fizemos uma análise detalhada para definir quais atributos seriam os mais eficazes e quais não seriam úteis. Isso foi feito com o objetivo de minimizar erros de variância, ruído e viés(Bias).

## Os Atributos presentes no nosso Data Set são:

GAME_DATE_EST = A data em que o jogo ocorreu.
GAME_ID = Número identificador do jogo
GAME_STATUS_TEXT = O status atual do jogo*
HOME_TEAM_ID = Número identificador do time da casa
VISITOR_TEAM_ID = Número identificador do time Visitante
SEASON = A temporada específica em que o jogo foi disputado*
PTS_home = O número de pontos marcados pelo time da casa durante o jogo.
FG_PCT_home = A porcentagem de arremessos de campo convertidos pelo time da casa
FT_PCT_home = A porcentagem de lances livres convertidos pelo time da casa
TEAM_ID = Número identificador do time
TEAM_ABBREVIATION =  A abreviação ou sigla oficial do time*
TEAM_CITY = A cidade de origem do time*
PLAYER_NAME = O nome completo do jogador*
NICKNAME = O apelido ou nome mais curto do jogador*
START_POSITION = A posição inicial do jogador no início do jogo; se estiver vazio, indica que o jogador começou no banco de reservas*
COMMENT = comentários*
MIN = Os minutos jogados pelo jogador em uma partida específica.
PLAYER_ID = Número identificador do jogador
LEAGUE_ID = Número identificador da liga* 
SEASON_ID = Número identificador da temporada
STANDINGSDATE =  data em que a classificação foi registrada*
CONFERENCE = Conferencia (apenas dois valores possíveis Leste ou Oeste)
TEAM = O nome completo da equipe*
G = O número total de jogos jogados pela equipe na temporada
W = O número total de vitórias da equipe na temporada
L = O número total de derrotas da equipe na temporada.
W_PCT = A porcentagem de vitórias da equipe na temporada
MIN_YEAR = O ano em que a equipe começou a participar do campeonato da NBA*
MAX_YEAR = O ano mais recente em que a equipe participou do campeonato da NBA*
YEARFOUNDED = O ano de fundação da equipe. *
ARENA = O nome do estádio onde a equipe joga.*
ARENACAPACITY = A capacidade do estádio onde a equipe joga.*
AST_home = Assistências feitas pelo time da casa durante o jogo.
REB_home = Rebotes conquistados pelo time da casa durante o jogo.
FG3_PCT_home = Porcentagem de cestas de 3 pontos convertidas pelo time da casa durante o jogo.
PTS_AWAY = Número de pontos marcados pelo time visitante durante o jogo.
FG_PCT_AWAY = Porcentagem de arremessos de campo convertidos pelo time visitante durante o jogo.
FT_PCT_AWAY = Porcentagem de lances livres convertidos pelo time visitante durante o jogo.
AST_away = Assistências feitas pelo time visitante durante o jogo.
REB_away = Rebotes conquistados pelo time visitante durante o jogo.
FG3_PCT_away = Porcentagem de cestas de 3 pontos convertidas pelo time visitante durante o jogo.
HOME_TEAM_WINS = Indica se o time da casa venceu o jogo, com valor binário 0 (se o time visitante venceu) ou 1 (se o time da casa venceu).
FGM = Número total de arremessos bem-sucedidos durante o jogo.
FGA = Número total de tentativas de arremesso durante o jogo.
FG_PCT = Porcentagem de arremessos convertidos durante o jogo.
FG3M = Número total de cestas de três pontos bem-sucedidas durante o jogo.
FG3A = Número total de tentativas de cesta de três pontos durante o jogo.
FG3_PCT = Porcentagem de cestas de três pontos convertidas durante o jogo.
FTM = Número total de lances livres bem-sucedidos durante o jogo.
FTA = Número total de tentativas de lance livre durante o jogo.
FT_PCT = Porcentagem de lances livres convertidos durante o jogo.
OREB = Número total de rebotes ofensivos capturados durante o jogo.
DREB = Número total de rebotes defensivos capturados pelo jogador durante o jogo.
REB = Número total de rebotes, incluindo rebotes defensivos e ofensivos, capturados pelo jogador durante o jogo.
AST = Número total de assistências realizadas pelo jogador durante o jogo.
STL = Número total de roubos de bola realizados pelo jogador durante o jogo.
BLK = Número total de bloqueios realizados pelo jogador durante o jogo.
TO = Número total de turnovers (reversões) cometidos pelo jogador durante o jogo.
PF = Número total de faltas individuais cometidas pelo jogador durante o jogo.
PTS = Número total de pontos marcados pelo jogador durante o jogo.
PLUS_MINUS = Estatística que indica a diferença entre pontos marcados pela equipe quando o jogador está em quadra e os pontos sofridos pela equipe quando o jogador está em quadra.
HOME_RECORD = O histórico de vitórias e derrotas do time da casa na temporada até o momento do jogo.*
ROAD_RECORD = O histórico de vitórias e derrotas do time visitante na temporada até o momento do jogo.*
RETURNTOPLAY = Este atributo parece não conter informações relevantes para análises, pois está vazio (NULL).*
OWNER = O proprietário ou proprietários do time.*
GENERALMANAGER = O Diretor Geral da equipe.*
HEADCOACH = O treinador principal da equipe.*
DLEAGUEAFFILIATION = A filiação da equipe à Liga de Desenvolvimento da NBA (NBA G League), se aplicável.*

* Atributos marcados com este símbolo foram considerados pela equipe desimportantes para a previsão de resultados

- É importante destacar que a tabela "players.csv" será mantida mas não utilizada como parte dos dados, mas apenas como listagem dos nomes e IDs de jogadores

- Um exemplo de como os dados se manifestam no dataset seria:
O jogo de ID 22200468 foi disputado no dia 21/12/2022, entre os times de ID 1610612737 (time da casa) e 1610612741 (time visitante). O placar ficou 108 a 110.
A porcentagem de arremessos convertidos foi de 50% para o visitante e 43% do time da casa.
Em um jogo, o time da casa teve 100% e o time visitante teve 77% de aproveitamento de lances livres. Isso poderia ser considerado uma anomalia caso analisarmos apenas os lances livres,
mas o resultado da partida é influênciado por mais atributos, logo essa análise seria imcopleta.
