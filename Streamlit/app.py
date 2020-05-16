import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from blinker import Signal
import os


class FileReference:
    def __init__(self, filename):
        self.filename = filename

def hash_file_reference(file_reference):
    filename = file_reference.filename
    return (filename, os.path.getmtime(filename))

def main():  
 
    # Título
    html_title = """
    <div style='background-color:#ffffff;text-align:center'>
    <p style='color:#000000;font-size:40px;'>AceleraDev Data Science</p>
    </div>
    """
    st.markdown(html_title, unsafe_allow_html=True)

    # Subtítulo
    html_subtitle = """
    <div style='background-color:#ffffff;text-align:center'>
    <p style='color:#000000;font-size:20px;'>Análise Exploratória de Dados</p>
    </div>
    """
    st.markdown(html_subtitle, unsafe_allow_html=True)

    # Imagem
    st.sidebar.image('Imagens/logo.png', use_column_width=True)

    # Tipos de arquivos
    file_types = ["csv", "xlsx"]


    # Upload dos dados
    file = st.sidebar.file_uploader('Carregando os dados (.csv ou xlsx)', type=file_types)

   
    @st.cache(hash_funcs={FileReference: hash_file_reference})
    def try_read_df(data):
        try:
            return pd.read_csv(data)
        except:
            return pd.read_excel(data)
    if file:
        df = try_read_df(file)

            
    # Tutorial:
    st.title("")
    if file is None:
        st.markdown('# **Tutorial**')
        st.video('Imagens/Tutorial.mp4')
   
    # Dataframe:
    if st.sidebar.checkbox('Visualizando o  dataFrame'):

        if file is None:
           st.error("Error: Nenhum arquivo foi selecionado")
        else:
            st.markdown('**Head**')
            st.dataframe(df.head(10))

            # Shape: Número de linhas e colunas.
            st.markdown('**Shape**')
            df_dim = st.radio('', ('linhas', 'colunas'))
            if df_dim == 'linhas':
                st.write(df.shape[0])
            else:
                st.write(df.shape[1])

    # Especificando as colunas que serão visualizadas.
    if st.sidebar.checkbox('Selecione as colunas que deseja visualizar'):
        if file is None:
            st.error("Error: Nenhum arquivo foi selecionado")
        else:
            all_columns = df.columns.tolist()
            selected_columns = st.multiselect('Selecione', all_columns)
            df_new = df[selected_columns]
            if not df_new.empty:
                st.dataframe(df_new)

    # Menu com as informações do dataframe.
    if  st.sidebar.checkbox('Informações sobre o dataframe'):
        if file is None:
            st.error("Error: Nenhum arquivo foi selecionado")
        else:
            exploration = pd.DataFrame({'name': df.columns,
                                    'type': df.dtypes,
                                    'amount': df.isna().sum(), 'percentage': (df.isna().sum() / df.shape[0]) * 100})

            info = st.sidebar.selectbox('',['Tipos dos dados','Describe','Dados faltantes'])
            if info == 'Tipos dos dados':
                st.markdown('**Tipo e quantidade**')
                st.write(exploration.type.value_counts())
                st.markdown('**Colunas do tipo int64**')
                st.markdown(list(exploration[exploration['type'] == 'int64']['name']))
                st.markdown('**Colunas do tipo float64**')
                st.markdown(list(exploration[exploration['type'] == 'float64']['name']))
                st.markdown('**Colunas do tipo object**')
                st.markdown(list(exploration[exploration['type'] == 'object']['name']))

            elif info == 'Describe':
                st.markdown('**Estatística descritiva das colunas numéricas**')
                st.write(df.describe())
                st.markdown('**Estatística descritiva das colunas categóricas**')
                st.write(df.describe(include=['O']))

            else:
                st.markdown('**Tabela com o percentual de dados faltantes**')
                if not (exploration[exploration['amount'] != 0][['type', 'percentage']]).empty:

                    st.table(exploration[exploration['amount'] != 0][['type', 'percentage']])
                else:
                    st.error('Dataset não possui dados faltantes!')
   
    # Visualização dos dados através de gráficos.
    if  st.sidebar.checkbox('Análise Gráfica'):
        if file is None:
            st.error("Error: Nenhum arquivo foi selecionado")
        else:
            plot_graphics = st.sidebar.selectbox('',['Gráfico de correlação','Distribuição da variável target'])
            if plot_graphics == 'Gráfico de correlação':
                fig, ax = plt.subplots(figsize=(8, 8))
                sns.heatmap(df.corr(), annot=True, ax=ax)
                st.pyplot()

            elif plot_graphics == 'Distribuição da variável target':
                option = st.selectbox('Selecione a variável target', df.columns) # Para dados do tipo "object" é plotado um gráfico barras.
                if df[option].dtype == object:
                    sns.set_style('darkgrid')
                    fig, ax = plt.subplots(figsize=(8, 8))
                    sns.countplot(x=df[option], data=df)
                    plt.xticks(rotation=90)
                    st.pyplot()  
                else:
                    sns.distplot(df[option], bins=10)  #  Para dados do tipo "int64" ou "float64" é plotado um histograma.
                    st.pyplot()

    # Informações sobre o desenvolvedor.
    if st.sidebar.checkbox('Sobre'):
        if file is None:
            st.error("Error: Nenhum arquivo foi selecionado")
        else:
            st.markdown("Desenvolvedor(a): **Karinne Cristina**")
            st.title("")
            st.write('Cientista de Dados júnior, trabalho no desenvolvimento de projetos utilizando técnicas de Análise Exploratória, Visualização de Dados e Machine Learning.')
            st.title("")
            st.markdown("**LinkedIn:** https://www.linkedin.com/in/karinnecristinapereira/")
            st.markdown("**GitHub:** https://github.com/karinnecristina/Data-Science")


if __name__ == "__main__":
    main()
