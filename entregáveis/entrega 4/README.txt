MINI TRABALHO 4: 
equipe: 1

Membros:
Artur Jackson Leal Fontinele - 211030943
Fause Carlos Mascarenhas Lustosa Junior - 211031691
Lorenzo de Lima Alves dos Santos - 190032821
Pedro Cabeceira de Freitas - 211043727
Rafael Kenji Taira - 190044128
Thiago França Vale Oliveira - 170119429 

Outliers
    ->A partir da temporada 2020/21 foi implementado os play in que é uma repescagem para os times que ficaram na 7 colocação até a 10. O sétimo joga contra o oitavo e quem ganha vai para os play off e o perdedor joga contra o vencedor do jogo entre o nono e décimo e quem ganhar vai para os play off. Como só temos dados de duas temporadas e é um total de 12 jogos nas duas temporadas, decidimos tirar pela baixa quantidade de jogos e por estar só em duas temporadas.
    
    ->Retiramos a temporadas 2022/2023 por estar incompleta,ou seja não possuía dados de todos os jogos, jogadores e etc.

    ->Foi observado jogadores que não entraram em campo em determinadas partidas e, mesmo que não no momento, serão desconsiderados caso algum dado individual seja utilizado.

    ->Encontramos algumas inconsistências nas novas tabelas feitas, pelo que analisamos que temos colunas inteiras vazias. 

    ->É necessário ressaltar a dificuldade do grupo em definir e detectar outros outliers, pois o resultados de jogos pode variar bastante mas ao mesmo tempo é muito frequente dentro do esporte,  e a performance de times também é algo que oscila bastante, principalmente quando comparada a performance nos playoffs e na temporada regular.

Normalização

    ->Segmentamos nossos dados, dos jogos, em duas tabelas, a primeira foi com os jogos da temporada regular e a segunda tabela com os jogos dos playoffs. Assim permitindo que nós utilizemos uma das tabelas como dados de treinamento e outra como dados de teste. Onde os jogos estão separados por temporadas.