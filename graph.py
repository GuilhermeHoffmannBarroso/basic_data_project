import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\User\Desktop\estagio_num_final\Estagio_ex_UE1.xlsx', sheet_name='Internal value', usecols=('Ano', 'Pais', 'Transações com a UE', 'Transações total'))

paises = df['Pais'].unique()
anos = df['Ano'].unique()

writer1 = pd.ExcelWriter('Entrega.xlsx', engine='xlsxwriter')
colunas = ['Commodity']

colunas.extend(anos)

def get_index (series, element):
    for q in range(len(series)):
        if series[q] == element:
            return q


for pais in paises:
    dfe = pd.DataFrame(columns=(colunas))
    dfi = pd.DataFrame(columns=(colunas))
    listapais_int = []
    listapais_ext = []
    for ano in anos:
        print(f'{pais} {ano}')
        listaano_int = []
        listaano_ext = []
        c_df = pd.read_excel(r'C:\Users\User\Desktop\estagio_num_final\Estagio_ex_UE1.xlsx', sheet_name=f'{pais}_{ano}', usecols=('Pais', 'Ano', 'Parceiro', 'Commodity', 'Valor FOB', 'E interno'))
        i = 0
        while len(listaano_int)<= 5:
            linhaano = []
            print(i)
            if c_df.at[i, 'E interno'] == 1:
                linhaano.append(c_df.at[i, 'Commodity'])
                linhaano.append(c_df.at[i, 'Valor FOB'])
                listaano_int.append(linhaano)
            i = i+1
        j = 0
        while len(listaano_ext) <= 5:
            linhaano = []
            if c_df.at[j, 'E interno'] == 1:
                linhaano.append(c_df.at[i, 'Commodity'])
                linhaano.append(c_df.at[i, 'Valor FOB'])
                listaano_ext.append(linhaano)
            j = j + 1

        listapais_int.append(listaano_int)
        listapais_ext.append(listaano_ext)
    for k in range(len(listapais_ext)):
        for l in range(len(listapais_ext[k])):
            if listapais_ext[k][l][0] not in dfe['Commodity']:
                ser=pd.Series([listapais_ext[k][l][0]])
                dfe['Commodity'].append(ser)

            dfe.at[get_index(dfe['Commodity'],listapais_ext[k][l][0]), f'{anos[k]}'] = listapais_ext[k][l][1]

        for k in range(len(listapais_int)):
            for l in range(len(listapais_int[k])):
                if listapais_int[k][l][0] not in dfe['Commodity']:
                    ser = pd.Series([listapais_int[k][l][0]])
                    dfi['Commodity'].append(ser)

                dfe.at[get_index(dfe['Commodity'],listapais_ext[k][l][0]), f'{anos[k]}'] = listapais_ext[k][l][1]

    dfe.to_excel(writer1, sheet_name=f'{pais}_ext')
    dfi.to_excel(writer1, sheet_name=f'{pais}_int')

writer1.close()
