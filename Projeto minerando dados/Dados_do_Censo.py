#!/usr/bin/env python
# coding: utf-8

# Dataset:
# O conjunto de dados para este projeto é originário do Repositório de A prendizado de Máquina da UCI
# (https://archive.ics.uci.edu/ml/datasets/Adult)

# Importando os módulos

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.model_selection import RandomizedSearchCV
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from warnings import simplefilter
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
simplefilter(action='ignore', category=FutureWarning)


# Carregando e visualizando os Dados

df = pd.DataFrame()
for chunk in pd.read_csv('adult.data', na_values='?', chunksize=100000):
    df = pd.concat([df, chunk])
df.head()

# Descrição das principais Features

# age: Idade.

# workclass: Classe trabalhadora. Se a pessoa é funcionário público, autônomo, empresário etc.
#
# education: Níveis de Escolaridade.
# 
# education-num: Código do Nível de Escolaridade.
# 
# marital-status: Estado Civil.
# 
# occupation: Ocupação (Suporte técnico, Conserto de arte, Outros serviços, Vendas, Exec-managerial,
# Prof-specialty, Manipuladores de limpeza, Machine-op-inspct, Adm-clerical, Pesca agropecuária,
# Transport-moving, Priv-house-serv, Serviço de Proteção, Forças Armadas)
# 
# relationship: Relacionamento (Esposa, Filha Própria, Marido, Não-familiar, Outro-parente, Solteira.)
# 
# race: Raça (Preto, branco, asiático-Pac-Islander, Amer-Indian-Eskimo, Outro.)
# 
# sex: Sexo(Feminino, Masculino).
# 
# capital-gain: Ganho de Capital.
# 
# capital-loss: Perda de Capital.
# 
# hours-per-week: Horas de trabalho por Semana.
# 
# native-country: País Nativo (Estados Unidos, Camboja, Inglaterra, Porto Rico,
# Canadá, Alemanha, EUA (Guam-USVI-etc), Índia, México, Portugal etc)

# Informações sobre as colunas

df.info()

# Variáveis numéricas.
df.describe()

# Variáveis categóricas.
df.describe(include=['O'])

# Análise Exporatória

# Distribuição das classes (variável income)
sns.catplot(x='income', kind='count', data=df, orient="h")
df['income'].value_counts()


# Distribuição das classes por Nível de Escolaridade
plt.figure(figsize=(20, 10))
sns.countplot(data=df, x='education',  hue='income')
plt.xticks(rotation=65)

df['education'].value_counts()

# Verificando a menor e a maior jornada de trabalho.
print(df['hours-per-week'].min())
print(df['hours-per-week'].max())

# Para uma melhor visualização vamos agrupar as horas trabalhadas em 3 categorias:
# 0-30 (jornada curta)
# 30-40 (jornada normal)
# 40-100 (jornada extra)

df['hours-per-week'] = pd.cut(df['hours-per-week'], [0, 30, 40, 100], labels=['short', 'normal', 'extra'])

# Distribuição das classes por Horas trabalhadas
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='hours-per-week',  hue='income')
plt.xticks(rotation=65)

df['hours-per-week'].value_counts()

# Distribuição das classes de acordo com a ocupação
plt.figure(figsize=(20, 10))
sns.countplot(data=df, x='occupation',  hue='income')
plt.xticks(rotation=65)

df['occupation'].value_counts()

# Relação das colunas age,sex e race com a coluna income.

plt.figure(figsize=(8, 6))
sns.countplot(y="sex", hue='income', data=df)

plt.figure(figsize=(8, 6))
sns.countplot(y="race", hue='income', data=df)

# Verificando a idade mínima e máxima do dataset.
print(f'A idade mínima é: {df.age.min()} anos')
print(f'A idade máxima é: {df.age.max()} anos')

# Para uma melhor visualização vamos agrupar as idades em 3 categorias:
# 0-25 anos (jovens)
# 25-50 anos (adultos)
# 50-100 anos (idosos)
df['age'] = pd.cut(df['age'], [0, 25, 50, 100], labels=['young', 'adult', 'old'])

# Verificando como ficou a distribuição.
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='age',  hue='income')
plt.xticks(rotation=70)

# Análise de Dados

# Verificando a quantidade de valores nulos no dataset.
total = df.isnull().sum().sort_values(ascending=False)
percent = df.isnull().sum()/df.isnull().count().sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, sort=False, keys=['total', 'percent'])
print(missing_data[missing_data['percent'] != 0])

# Preenchendo os valores nulos da coluna 'workclass'.
top = 'Private'
df['workclass'] = df['workclass'].fillna(top)

# Preenchendo os valores nulos da coluna 'occupation'.
top = 'United-States'
df['occupation'] = df['occupation'].fillna(top)

# Preenchendo os valores nulos da coluna 'native-country'.
top = 'Prof-specialty'
df['native-country'] = df['native-country'].fillna(top)

# Verificando se ainda existem valores nulos no Dataset.
if df.isnull().sum().sort_values(ascending=False).any() != 0:
    print(f'Existe valores nulos no dataset? {True}')
else:
    print(f'Existe valores nulos no dataset? {False}')

# Criando uma nova coluna com a renda final.
df['capital_last'] = df['capital-gain'] - df['capital-loss']

# Removendo as features irrelevantes.
# A coluna 'educational-num' está preenchida com o código referente a cada nível de escolaridade,
# dessa maneira podemos excluir a coluna 'education'.
# As colunas 'capital-gain' e 'capital-loss' estão representadas pela nova coluna que criamos anteriormente.


def remove_features(lista_features):
    for i in lista_features:
        df.drop(i, axis=1, inplace=True)


remove_features(['capital-gain', 'capital-loss', 'education'])

# Trasnformando as variáveis categóricas em numéricas.
cols = df[df.select_dtypes(['object']).columns]
for c in cols:
    encoding = LabelEncoder()
    encoding.fit(list(df[c].values))
    df[c] = encoding.transform(list(df[c].values))
df = pd.get_dummies(df)
df.head()

# Matriz de correlação

# Possibilita a análise simultânea da associação entre variáveis.
corr = df.corr()
sns.set(rc={'axes.facecolor': 'white', 'figure.facecolor': 'white'})
plt.subplots(figsize=(12, 9))
sns.heatmap(corr, vmax=.8, annot_kws={'size': 10}, annot=True, fmt='.2f')

corr_list = corr['income'].sort_values(axis=0, ascending=False).iloc[1:]
print(corr_list)

# Verificando as features mais importantes para o modelo.

# Separando a classe dos Dados.
previsores = df.drop('income', axis=1)
classe = df['income']

clf = RandomForestClassifier(n_estimators=100, random_state=7)
clf.fit(previsores, classe)

feature_imp = pd.Series(clf.feature_importances_, index=previsores.columns).sort_values(ascending=False)
print(feature_imp)

plt.figure(figsize=(8, 6))
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.show()

# Selecionando as features de maior importância.
features_selected = []
for feature, importance in feature_imp.iteritems():
    if importance > 0.03:
        print(f'{feature}: {round(importance * 100)}%')
        features_selected.append(feature)

# Treinando os modelos utilizando apenas as features selecionadas.
previsores = df[features_selected]
classe = df['income']

# Avaliação dos modelos de Machine Learning

# Criando modelo de Machine Learning a partir de cada algoritmo
# Os dados estão em diferentes escalas e isso pode prejudicar a performance de alguns algoritmos.
# Vamos aplicar a  Padronização ao conjunto de dados (colocando-os na mesma escala).
# Nesta técnica, os dados serão transformados de modo que estejam com uma distribuição normal, com média igual a zero e
# desvio padrão igual a 1.

# Não utilizarei o modelo SVC, pois ele não funciona bem quando temos um grande conjunto de dados
# porque o tempo de treinamento necessário é maior. 

pipelines = []
pipelines.append(('Scaled-LR', Pipeline([('Scaler', StandardScaler()), ('LR', LogisticRegression())]))),
pipelines.append(('Scaled-KNN', Pipeline([('Scaler', StandardScaler()), ('KNN', KNeighborsClassifier())]))),
pipelines.append(('Scaled-CART', Pipeline([('Scaler', StandardScaler()), ('CART', DecisionTreeClassifier())]))),
pipelines.append(('Scaled-NB', Pipeline([('Scaler', StandardScaler()), ('NB', GaussianNB())]))),
# pipelines.append(('Scaled-SVM', Pipeline([('Scaler', StandardScaler()),('SVM', SVC())])))
pipelines.append(('Scaled-RF', Pipeline([('Scaler', StandardScaler()), ('RF', RandomForestClassifier())])))
resultados = []
nomes = []

# Percorrendo cada um dos modelos
for nome, modelo in pipelines:
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=7)
    cross_val_result = model_selection.cross_val_score(modelo, 
                                                       previsores,
                                                       classe,
                                                       cv=kfold,
                                                       scoring='accuracy')
    resultados.append(cross_val_result)
    nomes.append(nome)
    texto = "%s: %f (%f)" % (nome, cross_val_result.mean(), cross_val_result.std())
    print(texto)

# De acordo com os resultados anteriores, os modelos criados com DecisionTree e Random Forest apresentaram 
# os melhores valores de acurácia e portanto os melhores resultados.
# Isso pode ser confirmado, comparando os algoritmos através de boxplots.
fig = plt.figure()
fig.suptitle('Comparando os Algoritmos Padronizados')
ax = fig.add_subplot(111)
plt.boxplot(resultados)
ax.set_xticklabels(nomes)
plt.show()

# Tunning dos modelos criados com Random Forest e DecisionTree.

# Embora o Random Forest tenha apresentado a menor taxa de erro após a padronização dos dados, podemos ainda otimizá-lo
# com o ajuste dos parâmetros.

# Definindo a escala
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

# Possíveis valores de estimators
val_estimators = [20, 50, 100, 150, 200]

# Possíveis valores para o critério de divisão
val_criterion = ['gini', 'entropy']

# Definindo um dicionário que recebe as listas de parâmetros e valores
parametros_grid = dict(n_estimators=val_estimators,
                       criterion=val_criterion)

# Criando o modelo
modelo_random = RandomForestClassifier()

# Definindo K
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=7)

# Testando diferenets combinações com os parâmetros
grid = RandomizedSearchCV(estimator=modelo_random, param_distributions=parametros_grid, cv=kfold, scoring='accuracy')
grid.fit(previsores, classe)

# Print do resultado
print("Grid scores on development set:")
means = grid.cv_results_['mean_test_score'].round(5)
stds = grid.cv_results_['std_test_score'].round(5)

for mean, std, params in zip(means, stds, grid.cv_results_['params']):
    print(f'mean:{mean},std:{std},params:{params}')
print()
print(f'Melhor parâmetro:{grid.best_params_}, Score:{grid.best_score_}')

# Vamos agora ajustar os parâmeros do DecisionTree.

# Definindo a escala
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

# Definindo a profundidade máxima da árvore.
max_depth = list(range(1, 31))

# Possíveis valores para o critério de divisão
val_criterion = ['gini', 'entropy']

# Definindo um dicionário que recebe as listas de parâmetros e valores
valores_grid = dict(criterion=val_criterion,
                    max_depth=max_depth)

# Criando o modelo
tree = DecisionTreeClassifier()

# Definindo K
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=7)

# Testando diferenets combinações com os valores de K
grid = RandomizedSearchCV(estimator=tree, param_distributions=valores_grid, cv=kfold, scoring='accuracy')
grid.fit(previsores, classe)

# Print do resultado  
print("Grid scores on development set:")
means = grid.cv_results_['mean_test_score'].round(5)
stds = grid.cv_results_['std_test_score'].round(5)

for mean, std, params in zip(means, stds, grid.cv_results_['params']):
    print(f'mean:{mean},std:{std},params:{params}')
print()
print(f'Melhor parâmetro:{grid.best_params_}, Score:{grid.best_score_}')

# Finalizando o Modelo
# O modelo criado com DecisionTree apresentou a melhor acurária entre todos os modelos criados
# e portanto será usado na construção da versão final do modelo preditivo.

# Preparando a versão final do modelo.
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)
modelo_tree = DecisionTreeClassifier(criterion='entropy', max_depth=14, random_state=7)
modelo_tree.fit(previsores, classe)
result_tree = cross_val_predict(modelo_tree, previsores, classe, cv=10)

print(f'Acurácia: {accuracy_score(classe,result_tree)}')
print('\n', confusion_matrix(classe, result_tree))
print('\n', classification_report(classe, result_tree))

# Fazendo a persistência do modelo treinado para o disco.

# filename = 'model_final.sav'
pickle.dump(modelo_tree, open('modelo.sav', 'wb'))
pickle.load(open('modelo.sav', 'rb'))
