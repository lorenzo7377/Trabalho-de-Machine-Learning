MINI TRABALHO 2: Aquisição de dados
equipe: 1

Membros:
Artur Jackson Leal Fontinele - 211030943
Fause Carlos Mascarenhas Lustosa Junior - 211031691
Lorenzo de Lima Alves dos Santos - 190032821
Pedro Cabeceira de Freitas - 211043727
Rafael Kenji Taira - 190044128
Thiago França Vale Oliveira - 170119429

- Nossos dados foram coletados na plataforma kaggle (https://www.kaggle.com/datasets/nathanlauga/nba-games).

- Os dados do nosso dataset foram obtidos na plataforma da NBA através de scripts coletados de jogos reais da NBA entre 2003 e 2022.

- Como essas informação estão sendo tiradas de um site público, não existe entre eles dados sensíveis.

## Engeharia de atributo

Nós utilizamos a engenharia de atributos (feature engineering) para separar os dados da nossa base de dados e deixar ela o mais limpa e apenas com os dados que serão necessários para a nossa análise. Conseguimos excluir uma coluna de status dos jogos, pois todos já acabaram e a coluna de id da liga, pois todos os jogos são da NBA, logo ela não agrega em nada.

## Normalização

Não achamos necessário utilizar a normalização, pois nossos dados não tem uma distância muito grande, eles variam de 0 até 150, independente da sua estatística, por exemplo, só vamos chegar perto de 100 quando é a pontuação de um jogo, mas a pontuação individuais não passam de 70 e os rebotes e assistências não passam de 20.

## Os Atributos presentes no nosso Data Set são:

GAME_DATE_EST = A data em que o jogo ocorreu.
GAME_ID = Número identificador do jogo
GAME_STATUS_TEXT = O status atual do jogo (todos estão final ent acho q n vamos usar)
HOME_TEAM_ID = Número identificado do time da casa
VISITOR_TEAM_ID = Número identificado do time Visitante
SEASON = A temporada específica em que o jogo foi disputado
PTS_home = O número de pontos marcados pelo time da casa durante o jogo.
FG_PCT_home = A porcentagem de arremessos de campo convertidos pelo time da casa
FT_PCT_home = A porcentagem de lances livres convertidos pelo time da casa
TEAM_ID = Número identificador do time
TEAM_ABBREVIATION =  A abreviação ou sigla oficial do time
TEAM_CITY = A cidade de origem do time
PLAYER_NAME = O nome completo do jogador
NICKNAME = O apelido ou nome mais curto do jogador
START_POSITION = A posição inicial do jogador no início do jogo; se estiver vazio, indica que o jogador começou no banco de reservas
COMMENT = comentários
MIN = Os minutos jogados pelo jogador em uma partida específica.
PLAYER_ID =Número identificado do jogador
LEAGUE_ID = Número identificado da liga (todos estão com vallor 00 então não devemos usar) 
SEASON_ID = Número identificado da temporada
STANDINGSDATE =  data em que a classificação foi registrada
CONFERENCE = Conferencia (apenas dois valores possíveis Leste ou Oeste)
TEAM = O nome completo da equipe
G = O número total de jogos jogados pela equipe na temporada
W = O número total de vitórias da equipe na temporada
L = O número total de derrotas da equipe na temporada.
W_PCT = A porcentagem de vitórias da equipe na temporada
MIN_YEAR = O ano em que a equipe começou a participar do campeonato da NBA
MAX_YEAR = O ano mais recente em que a equipe participou do campeonato da NBA
YEARFOUNDED = O ano de fundação da equipe.
ARENA = O nome do estádio onde a equipe joga.
ARENACAPACITY = A capacidade do estádio onde a equipe joga.
