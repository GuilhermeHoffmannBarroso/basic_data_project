from list2 import *
import pandas as pd

writer = pd.ExcelWriter('Estagio_ex_UE1.xlsx', engine='xlsxwriter')

df1 = pd.DataFrame(final_list, columns=('Ano', 'Pais', 'Transações com a UE', 'Transações total'))
df1.to_excel(writer, sheet_name='Internal value')

for l in range(len(final_list2)):
    df2 = pd.DataFrame(final_list2[l][2], columns=('Pais', 'Ano', 'Parceiro', 'Commodity', 'Valor FOB', 'E interno'))
    df2.to_excel(writer, sheet_name=f'{final_list2[l][0]}_{final_list2[l][1]}')

writer.close()