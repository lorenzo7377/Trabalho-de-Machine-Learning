MINI TRABALHO 5: Seleção dos potenciais modelos
equipe: 1

Membros:
Artur Jackson Leal Fontinele - 211030943
Fause Carlos Mascarenhas Lustosa Junior - 211031691
Lorenzo de Lima Alves dos Santos - 190032821
Pedro Cabeceira de Freitas - 211043727
Rafael Kenji Taira - 190044128
Thiago França Vale Oliveira - 170119429

##Potenciais Modelos:

Regressão Logística: A regressão logística é um algoritmo de aprendizado de máquina amplamente utilizado para problemas de classificação binária. Ela tem como objetivo estimar a probabilidade de uma fator pertencer a determinada classe, Isso é feito através da aplicação da função logística, também conhecida como função sigmoide, que transforma a saída do modelo em valores entre 0 e 1, representando as probabilidades. Este método é particularmente útil quando as relações entre as variáveis independentes e dependentes não são lineares, e é comumente empregado em campos como medicina, finanças e marketing para prever resultados binários e entender a influência relativa de cada variável no processo de tomada de decisão.

Justificativa: Escolhemos a regressão logística como um potencial modelo a ser usado em nosso projeto devido ao nosso projeto ter como finalidade uma classificação binária de que o time vai vencer ou não. Onde o modelo logístico se adequa como uma potencial solução para o problema.


Random Forests: Random Forest é um algoritmo de aprendizado de máquina que cria uma coleção de árvores de decisão durante o treinamento, onde cada árvore é construída a partir de uma amostra aleatória dos dados e uma seleção aleatória de características. Durante a previsão, a resposta final é determinada pela votação ou média das respostas das árvores individuais, resultando em um modelo robusto e preciso, menos suscetível ao overfitting. É amplamente utilizado para classificação e regressão em conjuntos de dados grandes e complexos

Justificativa: Mesmo sem ter muito conhecimento sobre o modelo que ainda não foi discutido em sala de aula, decidimos pesquisar sobre o Random Forest. Descobrimos que ele pode ser benéfico para o nosso trabalho, pois é capaz de detectar padrões complexos e lidar com múltiplas características dos dados. Isso nos pareceu útil, considerando a quantidade de características presentes no nosso database.


##Análise de Desempenho: 

Regressão Logística:

Utilizamos os atributos  FG_PCT_home (Porcentagem de arremessos de campo do time da casa), FT_PCT_home (Porcentagem de cestas de lance livre do time da casa), FG3_PCT_home (Porcentagem de cestas de 3 pontos do time da casa), AST_home (Assistências do time da casa), REB_home (Rebotes do time da casa), FG_PCT_away (Porcentagem de arremessos de campo do time visitante), FT_PCT_away (Porcentagem de cestas de lance livre do time visitante), FG3_PCT_away (Porcentagem de cestas de 3 pontos do time visitante), AST_away (Assistências do time visitante), REB_away (Rebotes do time visitante)

Se o resultado da previsão for 0 significa que o time visitante ganhou. Se for 1 então o time da casa ganhou a partida.

    -Ao fazer o teste com o modelo de regressão logística obtivemos os seguintes resultados:
    -Acurácia de 80%
    -Matriz de Confusão:
    -|83	34  |
    -|15	114|

    -Foram 83 verdadeiros positivos, 34 falsos positivos, 15 falsos negativos e 114 verdadeiros negativos.
    -Também tivemos outras métricas como f1-score e o recall que estão demonstradas na imagem anexada. Onde o f1-score do time da casa perder foi 0.77 e do time da casa vencer foi de 0.82. Já o recall para a derrota do time da casa foi de 0.71 e para vitória foi de 0.88.


O modelo mostra ser mais confiável em prever derrotas do time da casa do que suas vitórias, possivelmente devido a características mais distintas ou consistentes quando o time da casa perde comparado a quando ganha.
A análise sugere que os atributos escolhidos para o modelo, como porcentagens de arremessos de campo e de lances livres, assistências e rebotes, são indicativos significativos dos resultados das partidas.
