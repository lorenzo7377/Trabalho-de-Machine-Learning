MINI TRABALHO 1: Definição do problema e contextualização
equipe: 1

Membros:
Lorenzo de Lima Alves dos Santos - 190032821
Pedro Cabeceira de Freitas - 211043727
Rafael Kenji Taira - 190044128

- Definição do problema: A partir dos dados de jogos da National Basketball Association (doravante chamada NBA), contando desde 2003 até a temporada 2021-2022, temos como objetivo conseguir prever o resultado de futuros jogos de todos os times, não se atentando a placar mas a qual time ganhou, de forma relativamente precisa.

- Considerando que o objetivo é prever os resultados de futuros jogos, de maneira geral, a métrica de avaliação seria acurácia/precisão (se igualam devido a falta de falsos negativos e verdadeiros negativos), visto que, como o modelo só consegue prever um resultado e acertar ou errar, não haverá falsos negativos e verdadeiros negativos, o que impossibilita o cálculo de sensibilidade e especificidade, e por consequência impede o F1-score e o ROC de serem calculados.

- A fim de avaliar as soluções encontradas, será utilizado o processo de Seleção de Atributos, ou Feature Selection, pois o dataset é composto por cinco tabelas com 81 colunas totais, mas com repetições, e este processo servirá para dizer se as informações dadas ao modelo foram releventes e não causaram overfiting.

- A matriz de confusão será utilizada para melhor visualização de falsos positivos e verdadeiros positivos, assim facilitando o cálculo de precisão.