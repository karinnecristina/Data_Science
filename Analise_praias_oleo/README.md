# Análise das praias atingidas pelas manchas de óleo no Nordeste.

Nos últimos meses o Brasil tem sofrido um grande impacto ambiental com o vazamento de petróleo cru que vem poluindo um grande número de praias no Nordeste, e que recentemente vem se espalhando para a região Sudeste. Então resolvi fazer uma análise para demonstrar os números assustadores desse impacto.

## **Desenvolvimento:**

Os dados para alimentar a minha aplicação (que no momento só roda localmente), foram extraídos do arquivo '2019-11-09_LOCALIDADES_AFETADAS.xlsx' que está disponível no site do Ibama <http://www.ibama.gov.br/manchasdeoleo-localidades-atingidas>. Quando fiz a minha análise esses eram os dados mais recentes.
 
 Com os dados em mãos procurei extrair o máximo de informações e responder algumas das seguintes questões:
 
 - Quantos estados já foram atingindos pela mancha?
 - Em quantas localidades a mancha já chegou?
 - Qual o número de municípios que foram atingidos?
 - Quais os estados atingidos pela mancha até o dia dessa análise?
 
 O Pandas é uma biblioteca do Python muito utilizada para análise de dados. Com ele podemos ler nossos dados, que é um arquivo XLSX (Excel), e começar a manipular, transformar e limpar, caso necessário. 

 Em nosso arquivo temos as seguintes colunas: localidade, loc_id, municipio, estado, Data_Avist, Latitude, Longitude, Data_Revis e Status.
 
 Para responder as questões acima não é necessário utilizar as colunas loc_id, Data_Revis e Status. Então, uma das alternativas é usar o Pandas para selecionar somente as colunas de nosso interesse.
 
 Com esses dados devidamente transformados e limpos criei o meu _dashboard_ (painel onde os gráficos são visualizados). Ele foi feito no Power BI que é uma das ferramentas para criação de planilhas e/ou gráficos.
 
Foram gerados os seguintes gráficos:
 
 * Gráfico de barras com os estados e a quantidade de localidades atingidas.
 * Mapa de calor exibindo os locais afetados.
 * Tabela onde pode-se selecionar um estado e visualizar no mapa os pontos onde as manchas se encontram, como mostra o GIF abaixo.
 
![](Aplicacao.gif)


## Algumas melhorias para futuras implementações:

- Coletar os dados em tempo real para alimentar os gráficos.
- Disponibilizar o dashboard na web.
- Fazer uma análise cronológica do aparecimento dessas manchas.













