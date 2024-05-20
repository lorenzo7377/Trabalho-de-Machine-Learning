Mini trabalho 6: Otimização e ajuste fino do sistema
equipe: 1
Membros:
Lorenzo de Lima Alves dos Santos - 190032821
Pedro Cabeceira de Freitas - 211043727
Rafael Kenji Taira - 190044128
Artur Jackson Leal Fontinele - 211030943
Fause Carlos Mascarenhas Lustosa Junior - 211031691
Thiago França Vale Oliveira - 170119429


Regressão Logística 


Para melhorar o nosso modelo de regressão logística, fizemos uma média dos pontos que estamos usando para fazer a previsão, para conseguirmos ter dados reais e não fictícios. Essa parte deu certo, pois conseguimos pegar os dados das nossas tabelas e fazer as médias dos dados. Após essa parte, como o nosso modelo estava com uma precisão de aproximadamente 80%, visamos obter melhores resultados ao tentar colocar os pontos de cada time para melhorar a precisão, porém, os resultados se provaram irreais ao chegar a 100% de precisão ao avaliar que o time que possui mais pontos sempre será o vencedor de uma partida.

_________________________________________________________________

Classification Report:
              precision    recall  f1-score   support


           0       0.73      0.86      0.79        35
           1       0.89      0.79      0.84        52


    accuracy                           0.82        87
   macro avg       0.81      0.82      0.81        87
weighted avg       0.83      0.82      0.82        87


Confusion Matrix:
[[30  5]
 [11 41]]

_______________________________________________________________




Random Forest 

Além da implementação utilizando Regressão Logística, também decidimos implementar o modelo de treino Random Forest.  Esse algoritmo de aprendizado de máquina é baseado em árvores de decisão, onde várias árvores são criadas e combinadas para tomar decisões. Ao fazer com que o algoritmo escolhesse entre todas as features no dataset somente da temporada regular usado para treinamento e teste, foi possível observar que tivemos bons valores de precisão e recall e f1-score para o modelo. Chegando na casa dos 90%. Nesse teste vimos as features mais importantes para que o algoritmo chegasse no resultado, e notamos que existe uma influência um pouco maior das features PTS_home e PTS_away comparada com as outras. Mostrando uma possível dependência nesses valores. Retirando esses valores as métricas diminuem para a casa dos 80%.
Agora, após esse teste, seguindo a proposta inicial, utilizamos o modelo do Random Forest usando uma tabela com os jogos da temporada regular 21/22 como treino e os jogos dos playoffs que estão em outra tabela como dados de teste. Neste caso, onde o resultado com o valor 0 significa que o time visitante venceu a partida e quando é 1, foi o time da casa. Tivemos os seguintes valores de métricas:

_____________________________________________________________

Classification Report:
              precision    recall  f1-score   support


           0       0.73      0.91      0.81        35
           1       0.93      0.77      0.84        52


    accuracy                           0.83        87
   macro avg       0.83      0.84      0.83        87
weighted avg       0.85      0.83      0.83        87


Confusion Matrix:
[[32  3]
 [12 40]]


Feature Importances:
                     importance
FG_PCT_home            0.192828
FG_PCT_away            0.172694
FG3_PCT_home           0.102955
FG3_PCT_away           0.089309
REB_home               0.074436
REB_away               0.070390
AST_away               0.058939
AST_home               0.056525
FT_PCT_away            0.049795
FT_PCT_home            0.043293
GAME_ID                0.038492
GAME_DATE_EST_day      0.029903
GAME_DATE_EST_month    0.016556
GAME_DATE_EST_year     0.003885
HOME_TEAM_ID           0.000000
VISITOR_TEAM_ID        0.000000

____________________________________________________________


Técnica de validação cruzada

	Para analisarmos os resultados e o desempenho dos nossos algoritmos utilizamos o Cross-Validation, também chamado de validação cruzada, um algoritmo cujo objetivo é dividir o conjunto de dados em partes (folds), geralmente k partes. Em seguida, o modelo é treinado k vezes, cada vez utilizando k-1 partes dos dados como conjunto de treinamento e o restante dos dados como conjunto de teste. Isso permite que cada parte dos dados seja usada tanto para treinamento quanto para teste em diferentes iterações.

no modelo de regressão logística os resultados obtidos foram Acurácia (Validação Cruzada): [0.82520325 0.84552846 0.7804878  0.85365854 0.82520325]

O primeiro score é 0.82520325.
O segundo score é 0.84552846
O terceiro score é 0.7804878
O quarto score é 0.85365854.
O quinto score é  0.82520325

Acurácia Média (Validação Cruzada): 0.8260162601626015

indicando que o modelo tem um desempenho razoavelmente consistente ao longo das diferentes partições do conjunto de dados na validação cruzada. A acurácia média de cerca de 0.826 sugere que o modelo está correto em aproximadamente 82,6% das previsões, em média, o que pode ser considerado bom dependendo do contexto do problema.

No modelo Random forests os resultados obtidos foram Cross-Validation Scores:
O primeiro score é 0.8089.
O segundo score é 0.8211.
O terceiro score é 0.8292.
O quarto score é 0.8943.
O quinto score é 0.8617.

Mean CV Score: 0.8430894308943089

Esses valores representam pontuações relativamente altas, o que geralmente indica um bom desempenho do modelo


Melhoria no desempenho do modelo



Após a implementação de melhorias nos modelos de Regressão Logística e Random Forest, observamos avanços significativos em relação ao desempenho anterior. Inicialmente, a média dos pontos utilizados na Regressão Logística, alcançamos uma precisão de cerca de 80%. No entanto, ao tentar prever os resultados das partidas baseadas nos atributos envolvendo pontos de cada time, encontramos um cenário onde a precisão atingiu 100%, o que não reflete a realidade. Onde acabamos por extrair esses valores já que estavam deixando os resultados enviesados, não correspondendo com a realidade. Random Forest provou ser um modelo robusto com uma capacidade notável de gerar previsões confiáveis, mesmo quando privado de algumas das features mais influentes (features de pontos ‘PTS_home’ e ‘PTS_away’). A dependência nas pontuações dos jogos, embora útil para aumentar a precisão, pode não ser ideal para um modelo que se pretende robusto e adaptável a diferentes condições de jogo. A validação cruzada mostrou uma acurácia média de 84.3%, indicando uma boa generalização do modelo além do conjunto de treinamento.




