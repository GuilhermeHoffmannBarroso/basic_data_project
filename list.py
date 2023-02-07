from Loader import *

final_list = []
final_list2 = []
#writer = pd.ExcelWriter('estnumex.xlsx', engine='xlsxwriter')


#the following loop will be used to synthesize the information contained in the loaded dataframes.
#we will make a list containing the total trade values, in each year, along with the
for country in countries:
    for year in years:
        #variables ext_tv and int_tv correspond to the trade value in the year with all countries outside and inside the eu respectively
        ext_tv = 0
        int_tv = 0
        final_line = []
        final_line2 = []
        final_line2.append(country)
        final_line2.append(year)
        list_cy =[]
        final_line.append(year)
        final_line.append(country)

        for i in range(len(main_data1.index)):
            print(f'progress {i/len(main_data1.index)}, in {country} in {year}')
            cy_line = []
            if main_data1.at[i, 'ReporterDesc'] == country and main_data1.at[i, 'PartnerDesc'] != 'World' and main_data1.at[i, 'RefYear'] == year:
                cy_line.append(country)
                cy_line.append(year)
                cy_line.append(main_data1.at[i, 'PartnerDesc'])
                cy_line.append(main_data1.at[i, 'CmdDesc'])
                cy_line.append(main_data1.at[i, 'Fobvalue'])
                cy_line.append(1)
                list_cy.append(cy_line)
                int_tv = int_tv+main_data1.at[i, 'Fobvalue']

            elif main_data1.at[i, 'ReporterDesc'] == country and main_data1.at[i, 'RefYear'] == year:
                cy_line.append(country)
                cy_line.append(year)
                cy_line.append(main_data1.at[i, 'PartnerDesc'])
                cy_line.append(main_data1.at[i, 'CmdDesc'])
                cy_line.append(main_data1.at[i, 'Fobvalue'])
                cy_line.append(0)
                list_cy.append(cy_line)
                ext_tv = int_tv + main_data1.at[i, 'Fobvalue']

        final_line.append(int_tv)
        final_line.append(ext_tv)
        final_list.append(final_line)
        list_cys = sorted(list_cy, key= lambda x: x[4], reverse=True)
        final_line2.append(list_cys)
        final_list2.append(final_line2)
