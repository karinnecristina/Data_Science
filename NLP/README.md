## Data Cleaning 

# Dataset _https://www.kaggle.com/jrobischon/wikipedia-movie-plots_
# Dataset _https://www.kaggle.com/karrrimba/movie-metadatacsv_

O objetivo principal era prever o gênero do filme com base na descrição da trama
utilizando o primeiro dataset, porém durante a análise dos dados observei que a coluna genêro desse dataset possui muitos valores incorretos como: números, palavras incorretas, palavras escritas fora da ordem e palavras com variação ortográfica mais que se referem à mesma coisa.

Durante os estudos de NLP (_Natural language processing_), conheci a biblioteca fuzzywuzzy que é usada para correspondência de string. No segundo dataset temos uma coluna que possui vários genêros e subgenêros de filmes e que já está devidamente limpa, peguei esses dados e através da biblioteca fuzzywuzzy apliquei a similaridade de strings no dataset onde os dados estão incorretos. Além de corrigir os prblemas que já foram citados acima consegui reduzir o número de genêros do meu dataset de 2265 valores únicos para 995 valores únicos.
