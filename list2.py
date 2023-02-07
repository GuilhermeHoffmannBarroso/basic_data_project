from list import *

for j in range(len(countries)):
    int_tv = 0
    ext_tv = 0

    final_line = []
    final_line.append(2020)
    final_line.append(countries[j])

    final_line2 = []
    final_line2.append(countries[j])
    final_line2.append(2020)
    list_cy = []

    for k in range(len(main_data2.index)):
        print(f'progress is {k/len(main_data2.index)} in {countries[j]}, 2020')
        cy_line = []
        if main_data2.at[k, 'ReporterDesc'] == countries[j] and main_data2.at[k, 'PartnerDesc'] != 'World':
            cy_line.append(countries[j])
            cy_line.append(2020)
            cy_line.append(main_data2.at[k, 'PartnerDesc'])
            cy_line.append(main_data2.at[k, 'CmdDesc'])
            cy_line.append(main_data2.at[k, 'Fobvalue'])
            cy_line.append(1)
            list_cy.append(cy_line)
            int_tv = int_tv + main_data1.at[k, 'Fobvalue']

        elif main_data2.at[k, 'ReporterDesc'] == countries[j]:
            cy_line.append(countries[j])
            cy_line.append(2020)
            cy_line.append(main_data2.at[k, 'PartnerDesc'])
            cy_line.append(main_data2.at[k, 'CmdDesc'])
            cy_line.append(main_data2.at[k, 'Fobvalue'])
            cy_line.append(0)
            list_cy.append(cy_line)
            ext_tv = ext_tv + main_data1.at[k, 'Fobvalue']

    final_line.append(int_tv)
    final_line.append(ext_tv)
    final_list.append(final_line)

    list_cys = sorted(list_cy, key= lambda x: x[4], reverse=True)
    final_line2.append(list_cys)
    final_list2.append(final_line2)
