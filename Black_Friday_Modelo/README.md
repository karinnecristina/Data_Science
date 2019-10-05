## Esse é um Hackathon da plataforma Analytics Vidhya 
  <https://datahack.analyticsvidhya.com>

Afim de adquirir insights para entender melhor os dados,foi feita a _análise exploratória de dados(EDA)_ que é uma das etapas imprescindíveis para uma melhor eficiência dos modelos preditivos. A análise se encontra  no meu repositório: <https://github.com/karinnecristina/Data-Science/tree/master/Black_Friday>

## **Problema de negócio:** Previsão de Vendas para Black Friday 

**Declaração do Problema**
Uma empresa de varejo "ABC Private Limited" deseja entender o comportamento de compra do cliente (especificamente, valor da compra) em relação a vários produtos de diferentes categorias. Eles compartilharam o resumo de compra de vários clientes para produtos de alto volume selecionados no mês passado.
O conjunto de dados também contém dados demográficos do cliente (idade, sexo, estado civil, tipo_de_ cidade, estado_de_cidade_cidade), detalhes do produto (id do produto e categoria do produto) e valor total da compra do mês passado.
Agora, eles desejam criar um modelo para prever o valor da compra do cliente em relação a vários produtos, o que os ajudará a criar uma oferta personalizada para clientes em relação a diferentes produtos.

# Dados
---

Variáveis                  |Definição
---------                  |---------
User_ID                    |ID do usuário
Product_ID                 |ID do produto
Gender                     |Sexo do usuário
Age                        |Idade do usuário
Occupation                 |Profissão (Mascarada)
City_Category              |Categoria da cidade (A, B, C)
Stay_In_Current_City_Years |Número de anos de permanência na cidade atual
Marital_Status             |Estado civil
Product_Category_1         |Categoria de produto (mascarada)
Product_Category_2         |O produto pode pertencer a outra categoria também (Mascarado)
Product_Category_3         |O produto pode pertencer a outra categoria também (Mascarado)
Purchase                   |Valor da compra (variável de destino)

No final, temos o valor real da compra para o conjunto de dados de teste, com base no qual suas previsões serão avaliadas. As submissões são pontuadas no erro quadrático médio da raiz (RMSE). O _RMSE_ é muito comum e é uma métrica de erro de uso geral adequada. Comparado ao erro médio absoluto, o RMSE pune erros grandes.
