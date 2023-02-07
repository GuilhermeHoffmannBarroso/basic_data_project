import pandas as pd

# the following lines read the files extracted from the Comtrade database, referring to exports in EU countries
# I was forced to split the data in two files, as the database limited downloaded data to 250k lines
main_data1 = pd.read_csv(r'tdp1',low_memory=False, sep = ',', encoding='latin1',usecols=["TypeCode","FreqCode","RefPeriodId","RefYear","RefMonth","Period","ReporterCode","ReporterISO","ReporterDesc","FlowCode","FlowDesc","PartnerCode","PartnerISO","PartnerDesc","Prtner2Code","Partner2ISO","Partner2Desc","ClassificationCode","ClassificationSearchCode","IsOriginalClassification","CmdCode","CmdDesc","AggrLevel","IsLeaf","CustomsCode","CustomsDesc","MosCode","MotCode","MotDesc","QtyUnitCode","QtyUnitAbbr","Qty","IsQtyEstimated","AltQtyUnitCode","AltQtyUnitAbbr","AtlQty","IsAltQtyEstimated","NetWgt","IsNetWgtEstimated","GrossWgt","IsGrossWgtEstimated","Cifvalue","Fobvalue","PrimaryValue","LegacyEstimationFlag","IsReported","IsAggregate"])
main_data2 = pd.read_csv(r'tdp2', low_memory=False, sep=',', encoding ='latin1', usecols=["TypeCode","FreqCode","RefPeriodId","RefYear","RefMonth","Period","ReporterCode","ReporterISO","ReporterDesc","FlowCode","FlowDesc","PartnerCode","PartnerISO","PartnerDesc","Prtner2Code","Partner2ISO","Partner2Desc","ClassificationCode","ClassificationSearchCode","IsOriginalClassification","CmdCode","CmdDesc","AggrLevel","IsLeaf","CustomsCode","CustomsDesc","MosCode","MotCode","MotDesc","QtyUnitCode","QtyUnitAbbr","Qty","IsQtyEstimated","AltQtyUnitCode","AltQtyUnitAbbr","AtlQty","IsAltQtyEstimated","NetWgt","IsNetWgtEstimated","GrossWgt","IsGrossWgtEstimated","Cifvalue","Fobvalue","PrimaryValue","LegacyEstimationFlag","IsReported","IsAggregate"])

#theese lists will be used later
countries = main_data1['ReporterDesc'].unique()
years = main_data1['RefYear'].unique()
if countries[26] == 'United Kingdom':
    print('True')

print('Ran File "Loader"')
