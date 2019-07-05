''' Descrição: Solução do desafio-05 - osprogramadores.com '''


import json
import pandas as pd


def main():
    '''Faz a leitura do arquivo JSON'''

    with open('funcionarios.json') as file:
        data = json.load(file)

    df_funcionario = pd.DataFrame.from_dict(data['funcionarios'])
    df_area = pd.DataFrame.from_dict(data['areas'])

    # Unindo os DataFrames
    data = pd.merge(df_funcionario, df_area, left_on="area", right_on="codigo")

    # Quem mais recebe na empresa
    def answer_one():
        funcionario = data[data['salario'] == data['salario'].max()]
        for i in funcionario.values:
            print(f"global_max|{i[2]} {i[4]}|{i[3]:.2f}")
    answer_one()

    # Quem menos recebe na empresa
    def answer_two():
        funcionario = data[data['salario'] == data['salario'].min()]
        for i in funcionario.values:
            print(f"global_min|{i[2]} {i[4]}|{i[3]:.2f}")
    answer_two()

    # Média salarial da empresa
    def answer_three():
        media = data['salario'].mean()
        print(f"global_avg|{media:.2f}")
    answer_three()

    # Quem mais recebe em cada área
    def answer_four():
        area = data.groupby('area').apply(lambda x: x[x['salario'] == x['salario'].max()])
        for i in area.values:
            print(f"area_max|{i[6]}|{i[2]} {i[4]}|{i[3]:.2f}")
    answer_four()

    # Quem menos recebe em cada área
    def answer_five():
        area = data.groupby('area').apply(lambda x: x[x['salario'] == x['salario'].min()])
        for i in area.values:
            print(f"area_min|{i[6]}|{i[2]} {i[4]}|{i[3]:.2f}")
    answer_five()

    # Média salarial de cada área
    def answer_six():
        media = data.groupby(['nome_y'], as_index=False)['salario'].mean().round({'salario': 2})
        for i, item in media.values:
            print(f"area_avg|{i}|{item:.2f}")
    answer_six()

    # Área(s) com o maior número de funcionários
    def answer_seven():
        funcao = ['count']
        area = data.groupby(['nome_y'], as_index=False)[['nome_y']].agg(funcao).apply(max, axis=1)
        valor = area.reset_index()
        print(f"most_employees|{valor.loc[0, 'nome_y']}|{valor.loc[0, 0]}")
    answer_seven()

    # Área(s) com o menor número de funcionários
    def answer_eight():
        funcao = ['count']
        area = data.groupby(['nome_y'], as_index=False)[['nome_y']].agg(funcao).apply(min, axis=1)
        valor = area.reset_index()
        print(f"least_employees|{valor.loc[2, 'nome_y']}|{valor.loc[2, 0]}")
    answer_eight()

    # Maiores salários para funcionários com o mesmo sobrenome
    def answer_nine():
        salarios = data.groupby('sobrenome').filter(lambda group: len(group) > 1).copy()
        sal = salarios.groupby('area').apply(lambda x: x[x['salario'] == x['salario'].max()])
        print(f"last_name_max|{sal.iloc[0,4]}|{sal.iloc[0,2]} {sal.iloc[0,4]}|{sal.iloc[0,3]:.2f}")
        print(f"last_name_max|{sal.iloc[1,4]}|{sal.iloc[1,2]} {sal.iloc[1,4]}|{sal.iloc[1,3]:.2f}")
    answer_nine()


if __name__ == '__main__':
    main()
