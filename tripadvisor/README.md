# Aprendendo a extrair informações de uma página web 

Nesse projeto usei o framework scrapy para extrair algumas informações do site Tripadvisor a respeito da **Lagoa do Paraíso** em **Jericoacoara(Ceará)** local que pretendo conhecer em breve.

Foram extraídas as seguintes informações:

- Nome da pessoa que comentou;
- Localização de onde essa pessoa mora;
- Título do comentário;
- Descrição do comentário;
- Data do comentário;
- Tipo de viagem.

<img src="Image/coment.png" >

**Ferramentas utilizadas:**
- Python 3 
- Scrapy

**observação:** A versão do python precisa ser superior a 3.5

### Preparando o ambiente:

- Criando um ambiente virtual

```pip install virtualenv```

```virtualenv nomeambiente```

- Instalando o scrapy

```conda install -c conda-forge scrapy```

### Estrutura do projeto:

No arquivo items.py e comentarios.py (esse último arquivo está na pasta spiders) você encontra toda a estrutura utilizada para o desenvolvimento do projeto os outros arquivos são criados automaticamente quando iniciamos o scrapy. 

### Exportando os dados:

Depois que os dados foram extraídos as informações foram salvas em arquivos .csv e .json, o intuito e deixar os dados devidamente preparados para uma análise mais profunda.

